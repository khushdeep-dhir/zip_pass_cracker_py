ZIP Password Cracker

This project provides a simple and intuitive ZIP Password Cracking tool. It includes two implementations:

Graphical User Interface (GUI) using Tkinter.
Command-Line Interface (CLI) for more straightforward usage.
The tool attempts to crack a password-protected ZIP file using a list of potential passwords provided in a text file.

!!! Educational purpose only, I am not responsible if misused !!!

Features
Two Modes:
GUI-based application (app.py) with an intuitive interface to select files and start the cracking process.
CLI-based application (cracker.py) for users who prefer command-line operations.
Supports large password lists, with efficient iteration and error handling.
Provides clear feedback:
Informs the user about incorrect files or missing passwords.
Displays the successful password or failure message.
Project Structure
plaintext
Copy code
.
├── app.py               # Main GUI-based application
├── cracker.py           # Command-line based password cracker
├── passwords.txt        # Sample password list for testing

File Descriptions

app.py:

GUI-based ZIP password cracking tool.
Allows users to:
Browse and select a ZIP file.
Browse and select a password list file.
Start the cracking process with clear progress and result messages.
Provides error handling for invalid files and unsuccessful attempts.
cracker.py:

CLI-based version of the password cracker.
Accepts inputs for the ZIP file and password list via the command line.
Outputs the status of the cracking process to the console.
Handles invalid ZIP files, missing files, and unexpected errors.
passwords.txt:

A sample list of potential passwords for testing the tool.
Replace or extend this file with your custom password list for actual use.

How to Use
1. GUI Application
Run the app.py script for a user-friendly GUI.

bash
Copy code
python app.py
Steps:

Click Browse to select a password-protected ZIP file.
Click Browse to select a text file containing potential passwords.
Click Start Cracking to begin the process.
The application will notify you if the password is found or not.

2. Command-Line Interface
Run the cracker.py script for a CLI experience.

bash
Copy code
python cracker.py
Steps:

Enter the path to the ZIP file.
Enter the path to the password list file.
The program will iterate through the passwords and output the result.

Requirements
Python 3.6+
Libraries:
tkinter (for GUI)
zipfile (built-in)

Example
Password List (passwords.txt):
plaintext
Copy code
12345
password
letmein
qwerty
admin
welcome
Successful Output (CLI):
plaintext
Copy code
Enter zip file to extract: test.zip
Provide list of passwords to use: passwords.txt
There are total 6 passwords to test.
Password found at line 3
Password is: letmein
GUI Example:
The GUI will display a success message when the correct password is found or notify the user if no password matches.

Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the functionality or add new features.
