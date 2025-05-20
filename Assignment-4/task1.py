# Read a File and Handle Errors
try:
    with open("sample.txt", "r") as file:
        print("File content:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    # Either change the filename in line 3 or remove the file to get below error
    print("Error: The file 'sample.txt' was not found.")