import pytest
from main import count_vowels

# def test_only_vowels():
#     assert count_vowels("aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ") == 30
#
# def test_no_vowels():
#     assert count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == 0
#
# def test_mixed_string():
#     assert count_vowels("Hello, Привет!") == 4  # 'e', 'o', 'и', 'е'
#     assert count_vowels("Python is fun! Питон - это весело!") == 10  # 'o', 'i', 'u', 'и', 'о', 'е', 'о', 'е', 'о'
#
# def test_empty_string():
#     assert count_vowels("") == 0
#
# def test_upper_and_lower_case():
#     assert count_vowels("AaEeIiOoUuАаЕеЁёИиОоУуЫыЭэЮюЯя") == 30


@pytest.fixture
def vowel_strings():
    return {
        "only_vowels": "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ",
        "no_vowels": "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ",
        "mixed_string_1": "Hello, Привет!",
        "mixed_string_2": "Python is fun! Питон - это весело!",
        "empty_string": "",
        "upper_and_lower_case": "AaEeIiOoUuАаЕеЁёИиОоУуЫыЭэЮюЯя"
    }

def test_only_vowels(vowel_strings):
    assert count_vowels(vowel_strings["only_vowels"]) == 30

def test_no_vowels(vowel_strings):
    assert count_vowels(vowel_strings["no_vowels"]) == 0

def test_mixed_string_1(vowel_strings):
    assert count_vowels(vowel_strings["mixed_string_1"]) == 4  # 'e', 'o', 'и', 'е'

def test_mixed_string_2(vowel_strings):
    assert count_vowels(vowel_strings["mixed_string_2"]) == 10  # 'o', 'i', 'u', 'и', 'о', 'е', 'о', 'е', 'о'

def test_empty_string(vowel_strings):
    assert count_vowels(vowel_strings["empty_string"]) == 0

def test_upper_and_lower_case(vowel_strings):
    assert count_vowels(vowel_strings["upper_and_lower_case"]) == 30