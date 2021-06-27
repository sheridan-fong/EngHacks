import subprocess, sys


s = subprocess.run("powershell.exe conda activate enghack; python main.py", shell=True)
print(s)