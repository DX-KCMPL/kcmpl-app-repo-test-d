import os

def delete_file(filename):
    # WARNING: This is vulnerable to command injection
    os.system("rm -rf " + filename)

if __name__ == "__main__":
    user_input = input("Enter the filename to delete: ")
    delete_file(user_input)

def delete_file(filename):
    # WARNING: This is vulnerable to command injection
    os.system("rm -rf " + filename)

if __name__ == "__main__":
    user_input = input("Enter the filename to delete: ")
    delete_file(user_input)
