# Python File Handling Assignment

This repository contains two Python scripts that demonstrate file handling using reading, writing, and appending data with proper error handling.

---

## 📘 Task 1: Read a File and Handle Errors

**Filename:** `task1_read_file.py`

### 🔹 Functionality:
- Opens a file named `sample.txt`.
- Prints its contents line by line.
- If the file does not exist, it displays an error message.

### 💻 Example Output:

#### ✅ If `sample.txt` exists:
Line 1: this is the sample text file.
line 2: It contain multiple file

#### ✅ If `sample.txt` does not exists:
error: File 'sample.txt' not found



---

## ✍️ Task 2: Write and Append Data to a File

**Filename:** `task2_write_append.py`

### 🔹 Functionality:
- Takes user input and writes it to `output.txt`.
- Prompts for additional input to append to the same file.
- Displays the final contents of the file.

### 💻 Example Output:

Enter text to write to the file: Hello, Python!

Data successfully written in the output.txt.

Enter additional text to append: Learning file handling in Python.

Data successfully appended.

Final content of output.txt:

Hello, Python!
Learning file handling in Python.
