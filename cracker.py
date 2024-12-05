import zipfile

def crack_password(password_list, obj):
    idx = 0
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("Password found at line", idx)
                    print("Password is", word.decode('utf-8', errors='ignore'))
                    return True
                except (RuntimeError, zipfile.BadZipFile):
                    continue
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    return False
    return False

if __name__ == '__main__':
    import os

    zip_file = input("Enter zip file to extract: ")
    password_list = input("Provide list of passwords to use: ")

    # Ensure files exist before proceeding
    if not os.path.exists(zip_file):
        print(f"Error: File '{zip_file}' does not exist.")
        exit(1)

    if not os.path.exists(password_list):
        print(f"Error: File '{password_list}' does not exist.")
        exit(1)

    try:
        with zipfile.ZipFile(zip_file) as obj:
            # Using sum(1 for _) for memory-efficient counting
            with open(password_list, 'rb') as f:
                cnt = sum(1 for _ in f)
            print(f"There are total {cnt} passwords to test.")

            if not crack_password(password_list, obj):
                print("Password not found in the list provided.")
    except zipfile.BadZipFile:
        print("Error: Not a valid zip file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
