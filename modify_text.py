try:
    # Reading from the original file
    with open(r"c:\Users\HP\Desktop\Python\week4\PLP-Python_wk4\input.txt", "r") as input_file:
        content = input_file.read()
    
    # Modifying the content (for instance, appending text)
    modified_content = content + "\n\n This Text has been added to the file."

    # Writing the modified content to a new file
    with open("output.txt", "w") as output_file:
        output_file.write(modified_content)

    print("File has been successfully read and modified!")
except FileNotFoundError:
    print("The file 'input.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
