# Python Basic Programs

This repository contains two beginner-level Python programs that demonstrate fundamental concepts like file handling, user input, and error management.

---

## Task 1: Read a File and Handle Errors

This program attempts to read a text file and print its contents line by line. It also gracefully handles the scenario where the file does not exist.

### Functionality:

- Tries to open and read a file named `sample.txt`.
- Prints each line in the file.
- Handles the `FileNotFoundError` and displays a user-friendly message if the file is missing.

### Sample Output:

```
File content:
This is a sample text file.
It contains multiple lines.
```

---

## Task 2: Write and Append Data to a File

This program writes user input to a file and then appends additional input. Finally, it reads and displays the content of the file.

### Functionality:

- Prompts the user to enter initial content and writes it to `output.txt`.
- Prompts for more input and appends it to the same file.
- Reads the entire file and prints its contents.

### Sample Output:

```
Enter initial data to write to the file: Hello, Python!
Data successfully written to output.txt
Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
```

---

## How to Run

1. Make sure you have Python installed (Python 3.x recommended).
2. Run the script.