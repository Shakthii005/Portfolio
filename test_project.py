
import pytest
from project import check_common_patterns, assess_complexity, provide_feedback

def test_check_common_patterns():
    assert check_common_patterns("Password123") == True
    assert check_common_patterns("securePass#") == False
    assert check_common_patterns("abc123") == True


def test_assess_complexity():
    assert assess_complexity("Password123") == (11, 3)
    assert assess_complexity("123456") == (6, 1)

    length, complexity_score = assess_complexity("Complex#Password123")
    print(f"Debug: length={length}, complexity_score={complexity_score}")

    assert assess_complexity("Complex#Password123") == (19, 4)  # Corrected the expected length

@pytest.mark.parametrize("length, complexity_score, expected_feedback", [
    (10, 4, ["Your password is strong!"]),
    (5, 2, ["Password should be at least 8 characters long.", "Password should include at least three of the following: uppercase letters, lowercase letters, digits, and special characters.", "Consider improving your password based on the above suggestions."]),
    (8, 3, ["Your password is strong!"]),
])
def test_provide_feedback(length, complexity_score, expected_feedback):
    feedback = provide_feedback(length, complexity_score)
    assert feedback == expected_feedback

if __name__ == "__main__":
    pytest.main()


