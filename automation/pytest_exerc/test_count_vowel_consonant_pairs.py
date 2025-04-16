from count_vowel_consonant_pairs import count_vowel_consonant_pairs
import pytest


@pytest.mark.parametrize("input_str, expected_count", [
    ("hello", 1),
    ("banana", 3),
    ("AEIOUbc", 5),
    ("", 0),
    ("12345", 0),
    ("PyThOn", 1),
    ("a!e@i#o$u%", 0),
    ("", 0),
    ("a!e@i#o$u%", 0),
    ("12345", 0),
    ("a", 0),
    ("b", 0),
    ("a1e2i3o4u", 0),
    (None, TypeError),
    (12345, TypeError),
    (["hello"], TypeError),
    ({"text": "hi"}, TypeError),
])
def test_count_vowel_consonant_pairs(input_str, expected_count):
    assert count_vowel_consonant_pairs(input_str) == expected_count


@pytest.mark.parametrize("invalid_input", [
    None,
    12345,
    ["hello"],
    {"text": "hi"}
    ])
def test_count_vowel_consonant_pairs_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        count_vowel_consonant_pairs(invalid_input)
