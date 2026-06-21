import pytest
from logic_utils import check_guess, parse_guess, get_range_for_difficulty


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "🎉" in message


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" (go LOWER)
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" (go HIGHER)
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# Tests for the range validation bug fix
class TestRangeValidation:
    """Test that out-of-range guesses are properly detected."""

    def test_parse_guess_zero_returns_valid_int(self):
        # parse_guess should accept 0 and return it as a valid integer
        ok, guess_int, err = parse_guess("0")
        assert ok is True
        assert guess_int == 0
        assert err is None

    def test_parse_guess_101_returns_valid_int(self):
        # parse_guess should accept 101 and return it as a valid integer
        ok, guess_int, err = parse_guess("101")
        assert ok is True
        assert guess_int == 101
        assert err is None

    def test_get_range_easy(self):
        # Easy difficulty should have range 1-20
        low, high = get_range_for_difficulty("Easy")
        assert low == 1
        assert high == 20

    def test_get_range_normal(self):
        # Normal difficulty should have range 1-100
        low, high = get_range_for_difficulty("Normal")
        assert low == 1
        assert high == 100

    def test_get_range_hard(self):
        # Hard difficulty should have range 1-50
        low, high = get_range_for_difficulty("Hard")
        assert low == 1
        assert high == 50

    def test_guess_zero_out_of_range_easy(self):
        # 0 is out of range for Easy (1-20)
        low, high = get_range_for_difficulty("Easy")
        ok, guess_int, _ = parse_guess("0")
        assert ok is True  # parse_guess accepts it
        assert guess_int < low  # But it's out of range (this was the bug)

    def test_guess_101_out_of_range_normal(self):
        # 101 is out of range for Normal (1-100)
        low, high = get_range_for_difficulty("Normal")
        ok, guess_int, _ = parse_guess("101")
        assert ok is True  # parse_guess accepts it
        assert guess_int > high  # But it's out of range (this was the bug)

    def test_guess_0_out_of_range_hard(self):
        # 0 is out of range for Hard (1-50)
        low, high = get_range_for_difficulty("Hard")
        ok, guess_int, _ = parse_guess("0")
        assert ok is True  # parse_guess accepts it
        assert guess_int < low  # But it's out of range (this was the bug)


# Tests for parse_guess edge cases
class TestParseGuess:
    """Test parse_guess function with various inputs."""

    def test_parse_guess_empty_string(self):
        ok, guess_int, err = parse_guess("")
        assert ok is False
        assert guess_int is None
        assert err == "Enter a guess."

    def test_parse_guess_none(self):
        ok, guess_int, err = parse_guess(None)
        assert ok is False
        assert guess_int is None
        assert err == "Enter a guess."

    def test_parse_guess_non_number(self):
        ok, guess_int, err = parse_guess("abc")
        assert ok is False
        assert guess_int is None
        assert err == "That is not a number."

    def test_parse_guess_float_string(self):
        # Should convert "50.5" to 50
        ok, guess_int, err = parse_guess("50.5")
        assert ok is True
        assert guess_int == 50
        assert err is None

    def test_parse_guess_valid_positive(self):
        ok, guess_int, err = parse_guess("42")
        assert ok is True
        assert guess_int == 42
        assert err is None

    def test_parse_guess_valid_negative(self):
        # Negative numbers should parse successfully
        ok, guess_int, err = parse_guess("-5")
        assert ok is True
        assert guess_int == -5
        assert err is None
