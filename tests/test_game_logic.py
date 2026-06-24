from email import message
import pytest

from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    
def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


@pytest.mark.parametrize("attempt_number", range(0, 8))
def test_score_win_all_permutations(attempt_number):
    """Test win scores for different attempt numbers.
    
    Scoring logic: First correct attempt = 100 points, every incorrect attempt = -10 points
    attempt_number represents the logical attempt (0-indexed):
    - attempt_number=0 is the 1st guess: 100 points (100 - 10*0)
    - attempt_number=1 is the 2nd guess: 90 points (100 - 10*1)
    - attempt_number=2 is the 3rd guess: 80 points (100 - 10*2)
    """
    # Calculate expected score: 100 - 10 * attempt_number
    expected_score = 100 - 10 * attempt_number
    result = update_score(0, "Win", attempt_number)
    assert result == expected_score, f"Failed at attempt_number {attempt_number}: expected {expected_score}, got {result}"
