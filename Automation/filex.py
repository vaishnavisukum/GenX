def main():
    data = ''''''
    file_hello = open("./hello.py","r")
    data = file_hello.read()
    file_hello.close()
    print(data)
    file_demo = open("demo.py","w")
    file_demo.write(data)
    file_demo.close()


if(__name__ == "__main__"):
    main()
