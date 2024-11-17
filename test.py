import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ") == 30

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == 0

def test_mixed_string():
    assert count_vowels("Hello, Привет!") == 4  # 'e', 'o', 'и', 'е'
    assert count_vowels("Python is fun! Питон - это весело!") == 10  # 'o', 'i', 'u', 'и', 'о', 'е', 'о', 'е', 'о'

def test_empty_string():
    assert count_vowels("") == 0

def test_upper_and_lower_case():
    assert count_vowels("AaEeIiOoUuАаЕеЁёИиОоУуЫыЭэЮюЯя") == 30