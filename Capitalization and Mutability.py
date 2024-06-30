def capitalize_word(word: str) -> str:
    if len(word) == 0:
        return word 
    return word[0].upper() + word[1:]