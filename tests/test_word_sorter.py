import pytest

from app.word_sorter import sort_words_from_text


@pytest.mark.parametrize(
    'raw_text, exp_result',
    [
        # 1 Простой текст
        ('He was a professor..',
         [(1, 'a'), (1, 'be -> was'), (1, 'he'), (3, 'professor')]),

        # 2 Дублирование слов
        ('He was was a professor professor..',
         [(1, 'a'), (1, 'be -> was'), (1, 'he'), (3, 'professor')]),

        # 3 Разные регистры, много пунктуации, несуществующих слов и цифр
        ('KEYBOARD; ./-=+CompUter, ttt 1234567890 internet: :; $%^&{}[]()_-- ',
         [(1, 'computer'), (2, 'internet'), (4, 'keyboard')]),

        # 4 Текст содержит одно несуществующее слово
        ('He was a profesorr..',
         [(1, 'a'), (1, 'be -> was'), (1, 'he')]),

        # 5 Текст состоит из несуществующих слов
        ('H wasa profesorr 123', None),

        # 6 Пустой текст
        ('', None)
    ]
)
def test_sort_words_from_text(word_storage, raw_text, exp_result):
    sorted_words = sort_words_from_text(raw_text, word_storage)
    assert sorted_words == exp_result


if __name__ == '__main__':
    pytest.main()
