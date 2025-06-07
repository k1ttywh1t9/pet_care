def camel_case_to_snake_case(input_str: str) -> str:
    """SubjectNameMentioned => subject_name_mentioned"""
    """AbbreviationABOBA => abbreviation_aboba"""
    """BEBRANotion => bebra_abbr"""

    chars = []
    for curr_idx, char in enumerate(input_str):
        if curr_idx and char.isupper():
            next_idx = curr_idx + 1

            # separate abbr flag
            flag = next_idx >= len(input_str) or input_str[next_idx].isupper()
            prev_char = input_str[curr_idx - 1]
            if prev_char.isupper() and flag:
                pass
            else:
                chars.append("_")
        chars.append(char.lower())
    return "".join(chars)
