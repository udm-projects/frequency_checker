from collections import defaultdict

from app.logger import logger
from app.utils.text import text_to_word_list
from app.word import Words


def sort_words_from_text(raw_text: str, word_storage: Words) -> list | None:
    """Преобразование текста в список слов, отсортированный
    по частоте употребления и алфавиту"""

    logger.info('Начало преобразования текста в отсортированный список слов')
    word_list = text_to_word_list(raw_text)
    if word_list:
        return sort_words_from_list(word_list, word_storage)
    else:
        logger.info('Текст не содержит слов для сортировки \n')
        return None


def sort_words_from_list(word_list: list, word_storage: Words) -> list | None:
    """Сортировка списка слов по частоте употребления и алфавиту"""
    words_by_frequency = group_word_list_by_frequency(word_list, word_storage)
    if words_by_frequency:
        sorted_word_list = get_sorted_word_list(words_by_frequency)
        logger.info('Текст преобразован в отсортированный список слов \n')
        return sorted_word_list
    else:
        logger.info('Ни одно слово из текста не найдено в справочнике слов \n')
        return None


def group_word_list_by_frequency(word_list: list,
                                 word_storage: Words) -> defaultdict:
    """Группировка списка слов по частоте употребления.
    Слова из текста сопоставляются с базой слов из файла"""
    words_by_frequency = defaultdict(list)
    for word in word_list:
        word_obj = word_storage.get_word_params_by_name(word)
        if word_obj:
            if word != word_obj.base_word_name:
                # если слово - производное от базового слова,
                # то отображать его вместе с базовым словом
                word = f'{word_obj.base_word_name} -> {word}'
            words_by_frequency[word_obj.base_word_frequency].append(word)
        else:
            logger.debug(f'Слово {word} не найдено в базе слов')
    return words_by_frequency


def get_sorted_word_list(words_by_frequency: dict) -> list:
    """Сортировка слов по частоте и алфавиту.
    На выходе получаем список кортежей
    в формате (частота употребления, слово)"""
    output_list = list()
    for word_freq in sorted(list(words_by_frequency.keys())):
        word_list = words_by_frequency[word_freq]
        for word in sorted(word_list):
            output_list.append((word_freq, word))
            # logger.debug(f'{word_freq}k: {word}')
    return output_list
