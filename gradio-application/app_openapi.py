import os
import typing as t
import requests
import gradio as gr

# === Настройки (без UI) ===
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000").rstrip("/")
TIMEOUT = (5, 45)  # connect, read


# === Клиент ===
class Api:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.s = requests.Session()
        self.token: t.Optional[str] = None

    def _url(self, path: str) -> str:
        if not path.startswith("/"):
            path = "/" + path
        return f"{self.base_url}{path}"

    def _headers(self) -> dict:
        h = {"Accept": "application/json"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        return h

    def req(self, method: str, path: str, *, params=None, json_=None, data=None, files=None):
        return self.s.request(
            method.upper(), self._url(path),
            headers=self._headers(),
            params=params or {},
            json=json_,
            data=data,
            files=files,
            timeout=TIMEOUT
        )

def ok(r: requests.Response) -> bool:
    return 200 <= r.status_code < 300

def msg_from(r: requests.Response) -> str:
    try:
        j = r.json()
        if isinstance(j, dict) and "detail" in j:
            return j["detail"]
    except Exception:
        pass
    if r.status_code in (401, 403): return "Требуется вход/доступ."
    if r.status_code == 413: return "Файл слишком большой."
    return f"Ошибка {r.status_code}"

def jget(r: requests.Response):
    try:
        if "application/json" in r.headers.get("content-type", ""):
            return r.json()
    except Exception:
        return None
    return None


# === Бизнес-операции (названия и пути скрыты от пользователя) ===
# Авторизация
def do_login(api: Api, email: str, password: str):
    data = {"username": email, "password": password, "grant_type": "password", "scope": ""}
    r = api.req("POST", "/api/v1/users/auth/login", data=data)
    if not ok(r):
        return api, "Не удалось войти: " + msg_from(r)
    api.token = (r.json() or {}).get("access_token")
    return api, "Вы вошли в систему."

def do_logout(api: Api):
    try:
        api.req("POST", "/api/v1/users/auth/logout")
    finally:
        api.token = None
    return api, "Вы вышли из системы."

def get_me(api: Api):
    r = api.req("GET", "/api/v1/users/me")
    if ok(r):
        js = r.json() or {}
        # показываем кратко и по-человечески
        name = js.get("email") or js.get("username") or "Пользователь"
        return f"Привет, {name}!"
    return "Не удалось получить профиль: " + msg_from(r)

# Питомцы
def pets_list(api: Api):
    r = api.req("GET", "/api/v1/pets/")
    if not ok(r):
        return [], {}, "Не удалось загрузить питомцев: " + msg_from(r)
    data = r.json() or []
    # ожидаем список
    if isinstance(data, dict):
        data = data.get("items") or data.get("results") or []
    names = []
    idx = {}
    for it in data:
        nm = str(it.get("name") or f"id:{it.get('id')}")
        names.append(nm)
        idx[nm] = int(it.get("id"))
    return names, idx, f"Найдено питомцев: {len(names)}"

def pet_create(api: Api, name: str):
    r = api.req("POST", "/api/v1/pets/", json_={"name": (name or "").strip()})
    return "Питомец создан." if ok(r) else ("Не удалось создать: " + msg_from(r))

def pet_update(api: Api, pet_id: int, new_name: str):
    r = api.req("PATCH", f"/api/v1/pets/{pet_id}", json_={"name": (new_name or '').strip()})
    return "Сохранено." if ok(r) else ("Не удалось сохранить: " + msg_from(r))

def pet_delete(api: Api, pet_id: int):
    r = api.req("DELETE", f"/api/v1/pets/{pet_id}")
    return "Удалено." if r.status_code == 204 or ok(r) else ("Не удалось удалить: " + msg_from(r))

def pet_upload_image(api: Api, pet_id: int, file_path: str | None):
    if not file_path:
        return "Файл не выбран."
    with open(file_path, "rb") as f:
        r = api.req("POST", f"/api/v1/images/pets/{pet_id}",
                    files={"image": (os.path.basename(file_path), f, "application/octet-stream")})
    return "Фото загружено." if ok(r) else ("Не удалось загрузить фото: " + msg_from(r))

# Заметки
def notes_for_pet(api: Api, pet_id: int):
    r = api.req("GET", "/api/v1/pet_notes/")
    if not ok(r):
        return [], "Не удалось загрузить заметки: " + msg_from(r)
    arr = r.json() or []
    if isinstance(arr, dict):
        arr = arr.get("items") or arr.get("results") or []
    notes = [n for n in arr if int(n.get("pet_id", -1)) == pet_id]
    labels = [f"#{n['id']}: {n.get('content','')[:80]}" for n in notes]
    return (labels, notes), f"Заметок: {len(labels)}"

def note_create(api: Api, pet_id: int, content: str):
    r = api.req("POST", "/api/v1/pet_notes/", json_={"pet_id": pet_id, "content": (content or "").strip()})
    return "Заметка добавлена." if ok(r) else ("Не удалось добавить: " + msg_from(r))

def note_delete(api: Api, note_id: int):
    r = api.req("DELETE", f"/api/v1/pet_notes/{note_id}")
    return "Удалено." if r.status_code == 204 or ok(r) else ("Не удалось удалить: " + msg_from(r))

# Расходы
def expenses_for_pet(api: Api, pet_id: int):
    r = api.req("GET", "/api/v1/expense_entries/")
    if not ok(r):
        return [], "Не удалось загрузить расходы: " + msg_from(r)
    arr = r.json() or []
    if isinstance(arr, dict):
        arr = arr.get("items") or arr.get("results") or []
    items = [x for x in arr if int(x.get("pet_id", -1)) == pet_id]
    labels = [f"#{x['id']}: {x.get('purpose','')} — {x.get('amount',0)}" for x in items]
    return (labels, items), f"Расходов: {len(labels)}"

def expense_create(api: Api, pet_id: int, amount: float, purpose: str):
    r = api.req("POST", "/api/v1/expense_entries/",
                json_={"pet_id": pet_id, "amount": int(amount or 0), "purpose": (purpose or "").strip()})
    return "Запись добавлена." if ok(r) else ("Не удалось добавить: " + msg_from(r))

def expense_delete(api: Api, entry_id: int):
    r = api.req("DELETE", f"/api/v1/expense_entries/{entry_id}")
    return "Удалено." if r.status_code == 204 or ok(r) else ("Не удалось удалить: " + msg_from(r))

# Медицинские записи
def med_for_pet(api: Api, pet_id: int):
    r = api.req("GET", "/api/v1/medical_records/")
    if not ok(r):
        return [], "Не удалось загрузить мед.записи: " + msg_from(r)
    arr = r.json() or []
    if isinstance(arr, dict):
        arr = arr.get("items") or arr.get("results") or []
    items = [x for x in arr if int(x.get("pet_id", -1)) == pet_id]
    labels = [f"#{x['id']}: {x.get('name','')}" for x in items]
    return (labels, items), f"Мед.записей: {len(labels)}"

def med_create(api: Api, pet_id: int, name: str):
    r = api.req("POST", "/api/v1/medical_records/", json_={"pet_id": pet_id, "name": (name or "").strip()})
    return "Запись добавлена." if ok(r) else ("Не удалось добавить: " + msg_from(r))

def med_delete(api: Api, rec_id: int):
    r = api.req("DELETE", f"/api/v1/medical_records/{rec_id}")
    return "Удалено." if r.status_code == 204 or ok(r) else ("Не удалось удалить: " + msg_from(r))

def med_upload_file(api: Api, rec_id: int, file_path: str | None):
    if not file_path:
        return "Файл не выбран."
    with open(file_path, "rb") as f:
        r = api.req("POST", f"/api/v1/files/medical_records/{rec_id}",
                    files={"file": (os.path.basename(file_path), f, "application/octet-stream")})
    return "Файл прикреплён." if ok(r) else ("Не удалось прикрепить: " + msg_from(r))


# === UI ===
with gr.Blocks(title="Мои питомцы") as demo:
    gr.Markdown("## 🐾 Мои питомцы")

    api_state = gr.State(Api(API_BASE_URL))
    pets_idx = gr.State({})        # name -> id
    notes_cache = gr.State([])     # список заметок (dicts)
    ex_cache = gr.State([])        # список расходов
    md_cache = gr.State([])        # список мед.записей

    # Вход
    with gr.Tab("Вход"):
        hello = gr.Markdown("")
        email = gr.Textbox(label="Email / логин")
        password = gr.Textbox(label="Пароль", type="password")
        with gr.Row():
            btn_login = gr.Button("Войти", variant="primary")
            btn_logout = gr.Button("Выйти", variant="stop")
        login_msg = gr.Markdown("")

        def _login(api: Api, em: str, pw: str):
            api, m = do_login(api, em, pw)
            greeting = get_me(api) if api.token else ""
            return api, (greeting or m), (m if not api.token else "")
        btn_login.click(_login, inputs=[api_state, email, password], outputs=[api_state, hello, login_msg])

        def _logout(api: Api):
            api, m = do_logout(api)
            return api, "", m
        btn_logout.click(_logout, inputs=[api_state], outputs=[api_state, hello, login_msg])

    # Питомцы
    with gr.Tab("Питомцы"):
        top_msg = gr.Markdown("")
        btn_reload = gr.Button("Обновить список")
        pet_dd = gr.Dropdown(choices=[], label="Выберите питомца", interactive=True)

        with gr.Accordion("➕ Добавить питомца", open=False):
            pet_name = gr.Textbox(label="Имя питомца")
            btn_add_pet = gr.Button("Добавить", variant="primary")
            add_msg = gr.Markdown("")

        with gr.Accordion("✏️ Изменить выбранного", open=True):
            new_name = gr.Textbox(label="Новое имя")
            with gr.Row():
                btn_save = gr.Button("Сохранить")
                btn_del = gr.Button("Удалить", variant="stop")
            edit_msg = gr.Markdown("")

        with gr.Accordion("📷 Фото питомца", open=False):
            pet_img = gr.File(label="Изображение", file_count="single")
            btn_img = gr.Button("Загрузить фото")
            img_msg = gr.Markdown("")

        # Заметки
        gr.Markdown("---")
        gr.Markdown("### Заметки")
        notes_msg = gr.Markdown("")
        notes_dd = gr.Dropdown(choices=[], label="Заметки", interactive=True)
        with gr.Row():
            note_text = gr.Textbox(label="Текст заметки")
            btn_note_add = gr.Button("Добавить", variant="primary")
            btn_note_del = gr.Button("Удалить", variant="stop")
        note_action_msg = gr.Markdown("")

        # Расходы
        gr.Markdown("---")
        gr.Markdown("### Расходы")
        ex_msg = gr.Markdown("")
        ex_dd = gr.Dropdown(choices=[], label="Расходы", interactive=True)
        with gr.Row():
            ex_amount = gr.Number(label="Сумма", precision=0, value=0)
            ex_purpose = gr.Textbox(label="Назначение")
            btn_ex_add = gr.Button("Добавить", variant="primary")
            btn_ex_del = gr.Button("Удалить", variant="stop")
        ex_action_msg = gr.Markdown("")

        # Медицинские записи
        gr.Markdown("---")
        gr.Markdown("### Медицинские записи")
        md_msg = gr.Markdown("")
        md_dd = gr.Dropdown(choices=[], label="Медицинские записи", interactive=True)
        with gr.Row():
            md_name = gr.Textbox(label="Название записи")
            btn_md_add = gr.Button("Добавить", variant="primary")
            btn_md_del = gr.Button("Удалить", variant="stop")
        with gr.Row():
            md_file = gr.File(label="Файл", file_count="single")
            btn_md_upload = gr.Button("Прикрепить файл")
        md_action_msg = gr.Markdown("")

        # wiring
        def _reload_pets(api: Api):
            names, idx, msg = pets_list(api)
            return msg, gr.update(choices=names, value=None), idx
        btn_reload.click(_reload_pets, inputs=[api_state], outputs=[top_msg, pet_dd, pets_idx])

        def _add_pet(api: Api, name: str):
            msg = pet_create(api, (name or "").strip())
            names, idx, rmsg = pets_list(api)
            new_val = names[-1] if names else None
            return msg + ("  " + rmsg if rmsg else ""), gr.update(choices=names, value=new_val), idx, gr.update(value="")
        btn_add_pet.click(_add_pet, inputs=[api_state, pet_name], outputs=[add_msg, pet_dd, pets_idx, pet_name])

        def _on_pet_selected(api: Api, idx_map: dict, chosen: str):
            if not chosen:
                # 10 выходов (см. список outputs ниже)
                return ("", "", gr.update(choices=[], value=None), [], "", gr.update(choices=[], value=None), [],
                        "", gr.update(choices=[], value=None), [])
            pet_id = int(idx_map[chosen])

            # заполняем имя
            nn = chosen

            # заметки
            (note_labels, note_items), nmsg = notes_for_pet(api, pet_id)

            # расходы
            (ex_labels, ex_items), emsg = expenses_for_pet(api, pet_id)

            # мед.записи
            (md_labels, md_items), mmsg = med_for_pet(api, pet_id)

            return (
                f"Выбран: {chosen}",
                nn,
                gr.update(choices=note_labels, value=None), note_items,
                emsg,
                gr.update(choices=ex_labels, value=None), ex_items,
                mmsg,
                gr.update(choices=md_labels, value=None), md_items
            )

        pet_dd.change(
            _on_pet_selected,
            inputs=[api_state, pets_idx, pet_dd],
            outputs=[top_msg, new_name, notes_dd, notes_cache, ex_msg, ex_dd, ex_cache, md_msg, md_dd, md_cache]
        )

        def _save_pet(api: Api, idx_map: dict, chosen: str, nn: str):
            if not chosen: return "Сначала выберите питомца."
            return pet_update(api, int(idx_map[chosen]), (nn or "").strip())
        btn_save.click(_save_pet, inputs=[api_state, pets_idx, pet_dd, new_name], outputs=[edit_msg])

        def _del_pet(api: Api, idx_map: dict, chosen: str):
            if not chosen: return "Сначала выберите питомца."
            msg = pet_delete(api, int(idx_map[chosen]))
            names, idx, rmsg = pets_list(api)
            return msg + ("  " + rmsg if rmsg else ""), gr.update(choices=names, value=None), idx
        btn_del.click(_del_pet, inputs=[api_state, pets_idx, pet_dd], outputs=[edit_msg, pet_dd, pets_idx])

        def _pet_img(api: Api, idx_map: dict, chosen: str, fobj):
            if not chosen: return "Сначала выберите питомца."
            return pet_upload_image(api, int(idx_map[chosen]), fobj.name if fobj else None)
        btn_img.click(_pet_img, inputs=[api_state, pets_idx, pet_dd, pet_img], outputs=[img_msg])

        # Заметки
        def _note_add(api: Api, idx_map: dict, chosen: str, text: str):
            if not chosen: return "Сначала выберите питомца."
            pet_id = int(idx_map[chosen])
            msg = note_create(api, pet_id, text or "")
            (labels, items), _ = notes_for_pet(api, pet_id)
            return msg, gr.update(choices=labels, value=None), items, gr.update(value="")
        btn_note_add.click(_note_add,
                           inputs=[api_state, pets_idx, pet_dd, note_text],
                           outputs=[note_action_msg, notes_dd, notes_cache, note_text])

        def _note_del(api: Api, chosen: str, note_choice: str, notes_raw: list[dict]):
            if not chosen: return "Сначала выберите питомца."
            if not note_choice: return "Выберите заметку для удаления."
            note_id = None
            for n in notes_raw:
                if note_choice.startswith(f"#{n['id']}:"):
                    note_id = n["id"]; break
            if note_id is None: return "Не удалось определить заметку."
            msg = note_delete(api, int(note_id))
            return msg
        btn_note_del.click(_note_del, inputs=[api_state, pet_dd, notes_dd, notes_cache], outputs=[note_action_msg])

        # Расходы
        def _ex_add(api: Api, idx_map: dict, chosen: str, amount: float, purpose: str):
            if not chosen: return "Сначала выберите питомца."
            pet_id = int(idx_map[chosen])
            msg = expense_create(api, pet_id, amount or 0, purpose or "")
            (labels, items), _ = expenses_for_pet(api, pet_id)
            return msg, gr.update(choices=labels, value=None), items, gr.update(value=0), gr.update(value="")
        btn_ex_add.click(_ex_add,
                         inputs=[api_state, pets_idx, pet_dd, ex_amount, ex_purpose],
                         outputs=[ex_action_msg, ex_dd, ex_cache, ex_amount, ex_purpose])

        def _ex_del(api: Api, chosen: str, choice: str, raw: list[dict]):
            if not chosen: return "Сначала выберите питомца."
            if not choice: return "Выберите запись для удаления."
            ex_id = None
            for x in raw:
                label = f"#{x['id']}: {x.get('purpose','')} — {x.get('amount',0)}"
                if label == choice:
                    ex_id = x["id"]; break
            if ex_id is None: return "Не удалось определить запись."
            return expense_delete(api, int(ex_id))
        btn_ex_del.click(_ex_del, inputs=[api_state, pet_dd, ex_dd, ex_cache], outputs=[ex_action_msg])

        # Медицинские записи
        def _md_add(api: Api, idx_map: dict, chosen: str, name: str):
            if not chosen: return "Сначала выберите питомца."
            pet_id = int(idx_map[chosen])
            msg = med_create(api, pet_id, name or "")
            (labels, items), _ = med_for_pet(api, pet_id)
            return msg, gr.update(choices=labels, value=None), items, gr.update(value="")
        btn_md_add.click(_md_add,
                         inputs=[api_state, pets_idx, pet_dd, md_name],
                         outputs=[md_action_msg, md_dd, md_cache, md_name])

        def _md_del(api: Api, choice: str, raw: list[dict], chosen: str, idx_map: dict):
            if not chosen: return "Сначала выберите питомца."
            if not choice: return "Выберите запись."
            rid = None
            for x in raw:
                if choice.startswith(f"#{x['id']}:"):
                    rid = x["id"]; break
            if rid is None: return "Не удалось определить запись."
            msg = med_delete(api, int(rid))
            pet_id = int(idx_map[chosen])
            (labels, items), _ = med_for_pet(api, pet_id)
            return msg, gr.update(choices=labels, value=None), items
        btn_md_del.click(_md_del,
                         inputs=[api_state, md_dd, md_cache, pet_dd, pets_idx],
                         outputs=[md_action_msg, md_dd, md_cache])

        def _md_upload(api: Api, choice: str, raw: list[dict], fobj):
            if not choice: return "Сначала выберите запись."
            rid = None
            for x in raw:
                if choice.startswith(f"#{x['id']}:"):
                    rid = x["id"]; break
            if rid is None: return "Не удалось определить запись."
            return med_upload_file(api, int(rid), fobj.name if fobj else None)
        btn_md_upload.click(_md_upload, inputs=[api_state, md_dd, md_cache, md_file], outputs=[md_action_msg])

# Запуск
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", "7860")))
