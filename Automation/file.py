import os
def main():
    message = ''''''
    next_line = True
    while next_line:
        line = input()
        if line.lower()=="exit":
            next_line = False
            break
        message = message+"\n"+line  
    print(message)  
    file = open("demo.py","w")
    file.write(message)
    file.close()
    os.system("python demo.py")
if (__name__ == "__main__"):
    main()
