def check_age(age):
    """Checks if the entered age is valid and its parity.

    Args:
        age: The age entered by the user as an integer.

    Returns:
        A string indicating the validity of the age and its parity.
    """

    if age < 0:
        return "Invalid age. Age cannot be negative."
    elif age > 120:
        return "Invalid age. Age seems too high."
    elif age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."

if __name__ == "__main__":
    while True:
        try:
            age = int(input("Enter your age: "))
            print(check_age(age))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")