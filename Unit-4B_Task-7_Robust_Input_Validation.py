# Custom Exception
class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter student marks (0-100): "))

    # Validate marks
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    # Check Pass/Fail
    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

except InvalidMarksError as e:
    print("Error:", e)

except ValueError:
    print("Error: Please enter a valid integer.")

finally:
    print("Program finished.")