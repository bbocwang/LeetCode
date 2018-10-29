class MinSliceWeight():
    def find(self,input):
        N = len(input)
        M=[[0 for _ in range(N)]for _ in range(N)]# inpormant!!!!
        for i in range(N):
            M[0][i]=input[0][i]
            print(M[0][i])
        for row in range(1,N):

            for col in range(N):
                if col == 0:
                    M[row][col]=input[row][col]+min(M[row-1][col],M[row-1][col+1])
                    #print(M[row-1][col],M[row-1][col+1])
                elif col == N-1:
                    M[row][col]=input[row][col]+min(M[row-1][col],M[row-1][col-1])
                else:
                    M[row][col]=input[row][col]+min(M[row-1][col],M[row-1][col-1],M[row-1][col+1])
                    #print(M[row-1][col],M[row-1][col-1],M[row-1][col+1])
                #print("M",row,col,"=",M[row][col])
                print(row,col,M)
        return min(M[N-1])

a=MinSliceWeight()
test=[
[1,4,7],
[4,5,6],
[7,8,9],
]
print(a.find(test))
