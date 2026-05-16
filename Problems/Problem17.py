def main():
     A = [[1,2],
         [3,4]]

     B = [[4,3],
         [2,1]]

     C=[]

     for i in range(2):
        row = []
        for j in range(2):
            total = 0
            for k in range(2):
                total = total + (A[i][k] * B[k][j])
            row.append(total)
        C.append(row)

     print(C)

if __name__ == "__main__":
    main()