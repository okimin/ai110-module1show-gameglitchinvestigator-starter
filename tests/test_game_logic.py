from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    # and tell the player to go LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    # and tell the player to go HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_compared_numerically_not_lexicographically():
    # Regression: a single-digit guess against a multi-digit secret must
    # compare numerically. 9 < 100 -> "Too Low". Under the old lexicographic
    # comparison, "9" > "100" wrongly returned "Too High".
    outcome, _ = check_guess(9, 100)
    assert outcome == "Too Low"
