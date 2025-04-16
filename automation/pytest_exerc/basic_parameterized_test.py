from count_vowel_consonant_pairs import count_vowel_consonant_pairs
import pytest


@pytest.mark.parametrize("input_str, expected_count", [
    ("hello", 1),
    ("banana", 3),
    ("AEIOUbc", 5),
    ("", 0),
    ("12345", 0),
    ("PyThOn", 1),
    ("a!e@i#o$u%", 0)
])
def test_count_vowel_consonant_pairs(input_str, expected_count):
    assert count_vowel_consonant_pairs(input_str) == expected_count
