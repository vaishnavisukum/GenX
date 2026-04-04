def main():
    print("enter a number ")
    no=int(input())

    # if no & 1 !=0:
    #     print("value is even ")
    # else:
    #     print("odd ")

    print(" even ") if no%2==0 else print("odd ") # terinary 
if __name__ == "__main__":
    main()