from count_vowel_consonant_pairs import count_vowel_consonant_pairs
import pytest


@pytest.mark.parametrize("input_str, expected_count", [
    ("a" * 1000 + "b" * 1000, 1),
    ("ab" * 1000, 1000),
])
def test_count_vowel_consonant_pairs_large_inputs(input_str, expected_count):
    assert count_vowel_consonant_pairs(input_str) == expected_count


def test_count_vowel_consonant_pairs_random_large_input():
    import random
    import string

    random_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10000))
    count_vowel_consonant_pairs(random_chars)

