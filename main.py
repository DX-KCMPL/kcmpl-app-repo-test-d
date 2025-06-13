import os

def vulnerable(user_input):
    os.system("ls " + user_input)  # 🚨 CodeQL will detect this as a command injection
