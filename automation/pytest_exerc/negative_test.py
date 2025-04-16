from count_vowel_consonant_pairs import count_vowel_consonant_pairs
import pytest


@pytest.mark.parametrize("invalid_input", [
    None,
    12345,
    ["hello"],
    {"text": "hi"}
])
def test_count_vowel_consonant_pairs_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        count_vowel_consonant_pairs(invalid_input)
