# Program to copy the contents of sample.txt to copy.txt

try:
    # Open source file and read content
    with open("sample.txt", "r") as source:
        content = source.read()

    # Open destination file and write content
    with open("copy.txt", "w") as destination:
        destination.write(content)

    print("File copied successfully from sample.txt to copy.txt")

except FileNotFoundError:
    print("Error: sample.txt file not found.")

except Exception as e:
    print("An error occurred:", e)