import pytest
from app.word import Words
from app.word_loader import load_words


@pytest.fixture(scope="session")
def word_storage():
    word_storage = Words()
    load_words(word_storage)
    return word_storage
