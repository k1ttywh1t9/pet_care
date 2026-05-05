import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 50 },  // 0 -> 50 пользователей
    { duration: '3m', target: 100 }, // 100 юзеров
    { duration: '1m', target: 0 },   // Спуск
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],   // Ошибок должно быть меньше 1%
    http_req_duration: ['p(95)<500'], // 95% запросов должны быть быстрее 500мс
  },
};

export default function () {
  // Используем переменную окружения для URL (удобно для CI/CD)
  const BASE_URL = __ENV.BASE_URL || 'http://localhost:8889';
  
  const res = http.get(`${BASE_URL}/health`);
  
  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  sleep(1); // Имитация паузы реального пользователя
}