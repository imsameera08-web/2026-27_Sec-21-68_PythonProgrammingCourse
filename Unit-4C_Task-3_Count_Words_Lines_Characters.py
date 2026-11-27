# Program to count lines, words, and characters in a text file

try:
    with open("sample.txt", "r") as file:
        content = file.read()

    # Count characters
    char_count = len(content)

    # Count words
    word_count = len(content.split())

    # Count lines
    with open("sample.txt", "r") as file:
        line_count = len(file.readlines())

    print("Number of Lines      :", line_count)
    print("Number of Words      :", word_count)
    print("Number of Characters :", char_count)

except FileNotFoundError:
    print("Error: sample.txt file not found.")

except Exception as e:
    print("An error occurred:", e)