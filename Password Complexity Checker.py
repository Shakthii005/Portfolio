
import re

# Function to check for common patterns
def check_common_patterns(password):
    common_patterns = ['123', 'abc', 'password', 'qwerty', '111', 'ABCD']  # Checking for common passwords
    for pattern in common_patterns:
        if pattern in password:
            return True
    return False

# Function to check if password is a phone number
def check_phone_number(password):
    if re.fullmatch(r'\d{10,15}', password):
        return True
    return False

# Function to check password complexity
def assess_complexity(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[@$!%*?&#]', password))

    complexity_score = sum([has_upper, has_lower, has_digit, has_special])

    return length, complexity_score

# Function to provide feedback on password strength
def provide_feedback(length, complexity_score):
    feedback = []

    if length < 8:
        feedback.append("Password should be at least 8 characters long.")

    if complexity_score < 3:
        feedback.append("Password should include at least three of the following: uppercase letters, lowercase letters, digits, and special characters.")

    if not feedback:
        feedback.append("Your password is strong!")
    else:
        feedback.append("Consider improving your password based on the above suggestions.")

    return feedback

# Main function to check password strength
def check_password_strength(password):
    if check_common_patterns(password):
        print("Password contains common patterns or sequences, making it weak.")
        return

    if check_phone_number(password):
        print("Password should not be a phone number. It is not safe.")
        return

    length, complexity_score = assess_complexity(password)

    feedback = provide_feedback(length, complexity_score)

    for message in feedback:
        print(message)

def main():
    print("Password Complexity Checker")
    while True:
        choice = input("1. Check Password Strength\n2. Exit\nEnter choice: ")

        if choice == '1':
            password = input("Enter the password: ")
            check_password_strength(password)

        elif choice == '2':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
