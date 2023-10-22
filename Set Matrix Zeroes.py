def setZeroes(self, matrix: list[list[int]]) -> None:
    a,b=len(matrix),len(matrix[0])
    first_col,first_row=False,False
    for i in range(a):
        if matrix[i][0]==0:
            first_col=True
    for j in range(b):
        if matrix[0][j]==0:
            first_row=True
    for i in range(1,a):
        for j in range(1,b):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0
    for i in range(1,a):
        if matrix[i][0]==0:
            for j in range(1,b):
                matrix[i][j]=0
    for i in range(1,b):
        if matrix[0][i]==0:
            for j in range(1,a):
                matrix[j][i]=0
    if first_col:
        for i in range(a):
            matrix[i][0]=0
    if first_row:
        for i in range(b):
            matrix[0][i]=0
    return matrix