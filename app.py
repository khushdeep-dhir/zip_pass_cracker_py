#imports
import tkinter as tk  
from tkinter import filedialog, messagebox  
import zipfile  

# Function to attempt password cracking
def crack_password(password_list_path, zip_file_path):
    """
    Tries to extract a ZIP file using passwords from a list.
    
    Args:
    - password_list_path: Path to the text file containing passwords.
    - zip_file_path: Path to the ZIP file to be cracked.
    """
    try:
        obj = zipfile.ZipFile(zip_file_path)        # Open the ZIP file
    except zipfile.BadZipFile:
        messagebox.showerror("Error", "Invalid ZIP file.")      # Show error if the file is not a valid ZIP
        return

    idx = 0  # Counter to keep track of line number
    with open(password_list_path, 'r') as password_file:        # Open the password list file
        passwords = password_file.readlines()           # Read all passwords into a list

    # Iterate through each password in the list
    for idx, password in enumerate(passwords, start=1):         # Start counting lines from 1
        password = password.strip()         # Remove any trailing whitespace or newline characters
        try:
            # Try to extract the ZIP file with the current password
            obj.extractall(pwd=password.encode('utf-8'))        # Encoding passwords to bytes 
            messagebox.showinfo("Success", f"Password found at line {idx}: {password}")         #success message
            return
        except (RuntimeError, zipfile.BadZipFile):
            continue        #Ignores incorrect passwords or other runtime errors

    messagebox.showwarning("Failed", "Password not found in the list.")          #Failed warning, if no pass found

# Function to browse for the ZIP file
def browse_zip():
    """
    Opens a file dialog to select a ZIP file and updates the zip_path variable.
    """
    zip_path.set(filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")]))  # File dialog for ZIP files

# Function to browse for the password list
def browse_password_list():
    """
    Opens a file dialog to select a text file and updates the password_list_path variable.
    """
    password_list_path.set(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]))  # File dialog for text files

# Function to initiate the password cracking process
def start_cracking():
    """
    Starts the password cracking process after validating input paths.
    """
    if not zip_path.get() or not password_list_path.get():          #Path checking
        messagebox.showwarning("Input Required", "Please select both files.")           #File missing warning
        return
    crack_password(password_list_path.get(), zip_path.get())        #call crack_password func

# GUI setup
root = tk.Tk()          #main app window
root.title("ZIP Password Cracker")      #window title

# Variables to store file paths
zip_path = tk.StringVar()               #StringVar to store the ZIP file path
password_list_path = tk.StringVar()     #StringVar to store the password list file path

# Layout for ZIP file selection
tk.Label(root, text="Select ZIP File:").grid(row=0, column=0, padx=10, pady=10)  # Label for ZIP file input
tk.Entry(root, textvariable=zip_path, width=40).grid(row=0, column=1, padx=10)  # Text entry for ZIP file path
tk.Button(root, text="Browse", command=browse_zip).grid(row=0, column=2, padx=10)  # Button to browse for ZIP file

# Layout for password list selection
tk.Label(root, text="Select Password List:").grid(row=1, column=0, padx=10, pady=10)  # Label for password list input
tk.Entry(root, textvariable=password_list_path, width=40).grid(row=1, column=1, padx=10)  # Text entry for password list path
tk.Button(root, text="Browse", command=browse_password_list).grid(row=1, column=2, padx=10)  # Button to browse for password list

# Button to start the cracking process
tk.Button(root, text="Start Cracking", command=start_cracking).grid(row=2, column=1, pady=20)  # Start button in the center

# Start the GUI main loop
root.mainloop()
