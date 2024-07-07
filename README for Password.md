Password Complexity Checker

Project Overview :

The Password Strength Checker is a Python-based application designed to evaluate the strength of user passwords and provide feedback for improving password security. This project integrates several key functionalities to assess password complexity, identify common weak patterns, and guide users towards creating stronger passwords. It serves as a valuable tool for enhancing personal cybersecurity by encouraging the use of robust passwords.

Key Features:

Common Patterns Detection:


Identifies and flags passwords containing common sequences or patterns such as '123', 'abc', 'password', and others.
Helps users avoid easily guessable passwords.
Phone Number Detection:

Checks if the password is a phone number, which is not secure.

Ensures passwords are not simple numeric sequences.
Password Complexity Assessment:

Evaluates the complexity of passwords based on several criteria:

Length of the password.

Presence of uppercase letters, lowercase letters, digits, and special characters.
Calculates a complexity score to determine password strength.
Feedback Provision:

Provides actionable feedback based on the assessed complexity:

Suggestions to meet minimum length requirements.
Recommendations for including diverse character types.
Confirmation if the password is strong.

Interactive User Interface:


A simple command-line interface for users to check the strength of their passwords.
User-friendly prompts guide users through the process of password evaluation.

Technical Implementation

Programming Language: Python

Libraries Used: re (regular expressions) for pattern matching.

Code Structure:


check_common_patterns: Checks for common patterns in passwords.

check_phone_number: Verifies if the password is a phone number.

assess_complexity: Assesses password complexity and calculates a complexity score.

provide_feedback: Provides feedback based on the length and complexity score of the password.

check_password_strength: Main function to evaluate password strength and display feedback.

main: Command-line interface for user interaction.
Testing
Testing Framework: pytest
Test Coverage:
Unit tests for each function to ensure accurate detection of common patterns, phone numbers, and password complexity.
Parameterized tests to cover a wide range of password scenarios.
Fixtures and assertions to verify the correctness of each function's output.
