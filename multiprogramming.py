import subprocess
def main():
    subprocess.Popen(["Python","script1.py"])
    subprocess.Popen(["Python","script2.py"])

if __name__ == "__main__":
    main()
#output 
#  C:\Users\Dell\Desktop\GenX>P1: hello world    both the program are simultateously executed
# P2 : Jay Ganesh                                 and the program which reaches first will be executed first
# P1: Done                                       thus when this program is executed multiple times it will show diff O/p
# P1: Completed