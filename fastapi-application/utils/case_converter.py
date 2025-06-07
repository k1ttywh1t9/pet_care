def camel_case_to_snake_case(input_str: str) -> str:
    """SubjectNameMentioned => subject_name_mentioned"""
    """AbbreviationABOBA => abbreviation_aboba"""
    """BEBRANotion => bebra_abbr"""

    chars = []
    for curr_indx, char in enumerate(input_str):
        if curr_indx and char.isupper():
            next_indx = curr_indx + 1

            # separate abbr flag
            flag = next_indx >= len(input_str) or input_str[next_indx].isupper()
            prev_char = input_str[curr_indx - 1]
            if prev_char.isupper() and flag:
                pass
            else:
                chars.append("_")
        chars.append(char.lower())
    return "".join(chars)
