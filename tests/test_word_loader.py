import pytest

from app.word import Word


@pytest.mark.parametrize(
    'target_word_name, exp_result',
    [
        # 1 Базовое слово, имеющее производные слова, частота - топ 1к
        ('nature',
         Word(name='nature', base_word_name='nature', base_word_frequency=1)),

        # 2 Слово, производное от базового nature, частота - топ 1к
        ('naturally',
         Word(name='naturally', base_word_name='nature', base_word_frequency=1)),

        # 3 Редкое слово(топ 21к), не имеющее производных слов
        ('chia',
         Word(name='chia', base_word_name='chia', base_word_frequency=21)),

        # 4 Несуществующее слово
        ('booklettt', None)
    ]
)
def test_load_words(word_storage, target_word_name, exp_result):
    # load_words() запускается в conftest
    word = word_storage.get_word_params_by_name(target_word_name)
    assert word == exp_result


if __name__ == '__main__':
    pytest.main()
