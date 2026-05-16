# [[2,3],
#  [1,9]]

def main():
    
    A = [[1,2,3],
         [3,4,5],]
    
    B = [[4,3,6],
         [2,1,9]]
    
    C = []

    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(0,len(A)):
            temp = []
            for j in range(0,len(A[0])):

                add = A[i][j]+B[i][j]
                temp.append(add)

            C.append(temp)

    else:
        print("Addittion is not possible")

    print(C)

if __name__ == "__main__":
    main()