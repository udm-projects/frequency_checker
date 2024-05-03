import string

translator = str.maketrans('', '', string.punctuation + string.digits)


def remove_punctuation_and_digits_from_text(text: str) -> str:
    """Удаление пунктуации и цифр из текста"""
    return text.translate(translator)


def text_to_word_list(raw_text: str) -> list:
    """Преобразование текста в список слов"""
    processed_text = remove_punctuation_and_digits_from_text(raw_text).lower()
    if processed_text:
        word_list = list(set(processed_text.split()))
        return word_list
    else:
        return []
