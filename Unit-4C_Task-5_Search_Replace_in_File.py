# Program to replace a word in a text file
# Example: Replace "Python" with "Java"

try:
    # Read the file content
    with open("sample.txt", "r") as file:
        content = file.read()

    # Replace the word
    updated_content = content.replace("Python", "Java")

    # Write the updated content back to the file
    with open("sample.txt", "w") as file:
        file.write(updated_content)

    print("Word replaced successfully.")

except FileNotFoundError:
    print("Error: sample.txt file not found.")

except Exception as e:
    print("An error occurred:", e)