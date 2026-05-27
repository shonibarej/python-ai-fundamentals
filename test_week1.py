import pytest
from week1 import analyse_text, load_config, filterby_word_length

#Tests for filte_by_length
def test_filter_by_length_basic():
    words = ["python", "ai", "engineer", "data"]
    result = filterby_word_length(words, 3)
    assert result == ["python", "engineer", "data"]


def test_filter_by_length_no_results():
    words = ["ai", "uk", "ml"]
    result = filterby_word_length(words, 3)
    assert result == []

def test_filter_by_length_empty_list():
    result = filterby_word_length([], 3)
    assert result == []

# Tests for analyse_text:
def test_analyse_text_word_count():
    result = analyse_text("the cat sat on the mat")
    assert result["word_count"] == 6

def test_analyse_text_unique_words():
    result = analyse_text("the cat sat on the mat")
    assert result["unique_word_count"] == 5

def test_analyse_text_most_common():
    result = analyse_text("the cat sat on the mat the")
    assert result["most_common_word"] == "the"

def test_load_config():
    result = load_config("config.json", ["model", "temperature"])
    assert result == {
    "model": "gpt-4o",
    "temperature": 0.0,
    "max_tokens": 1000,
    "tags": [
        "rag",
        "production",
        "uk"
    ]
    }


    def test_load_config_missing_key():
        with pytest.raises(ValueError):
            load_config("config.json", ["model", "life"])