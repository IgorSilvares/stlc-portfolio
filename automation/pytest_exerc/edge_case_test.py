from count_vowel_consonant_pairs import count_vowel_consonant_pairs
import pytest


@pytest.mark.parametrize("input_str, expected_count", [
    ("", 0),
    ("a!e@i#o$u%", 0),
    ("12345", 0),
    ("a", 0),
    ("b", 0),
    ("a1e2i3o4u", 0)
])
def test_count_vowel_consonant_pairs_edge_cases(input_str, expected_count):
    assert count_vowel_consonant_pairs(input_str) == expected_count
