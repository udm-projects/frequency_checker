from dataclasses import dataclass


@dataclass(frozen=True)
class Word:
    name: str  # слово(может быть производным от базового слова)
    base_word_name: str  # базовое слово
    base_word_frequency: int  # частота употр. базового слова(топ от 1к до 25к)


class Words:
    def __init__(self):
        self._word_by_name = dict()

    def add_word(self, word: Word):
        self._word_by_name[word.name] = word

    def update_words(self, word_dict: dict[str, Word]):
        self._word_by_name.update(word_dict)

    def get_word_params_by_name(self, name: str) -> Word:
        return self._word_by_name.get(name)

    def get_words(self) -> dict[str, Word]:
        return self._word_by_name

    def get_count(self) -> int:
        return len(self._word_by_name)
