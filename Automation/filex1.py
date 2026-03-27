def main():
    file = open("Hello.py","r")
    data = file.read()
    file.close()
    print(data)

if(__name__ == "__main__"):
    main()
