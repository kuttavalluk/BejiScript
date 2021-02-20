import os

#atelmarkascript
if os.name == 'nt':
    os.system("cd BejiScript && cd IFB && python print.py")
if os.name == 'posix':
    os.system("cd BejiScript && cd IFB && python3 print.py")

if os.name == 'nt':
    os.system("cd BejiScript && cd IFB && python dictattack.py")
if os.name == 'posix':
    os.system("cd BejiScript && cd IFB && python3 dictattack.py")
