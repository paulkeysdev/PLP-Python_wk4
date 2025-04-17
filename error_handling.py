filename = input("Enter the filename: ")

try:
    # Attempt to read the file
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to access '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")
