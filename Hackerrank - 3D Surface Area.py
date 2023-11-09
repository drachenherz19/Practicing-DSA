def surfaceArea(A):

    # Write your code here
    x, y = len(A), len(A[0])
    sum = 2 * x * y
    for i in range(x):
        for j in range(y):
            if i > 0:
                sum += abs(A[i][j] - A[i-1][j])
            else:
                sum += A[i][j]
            if j > 0:
                sum += abs(A[i][j] - A[i][j-1])
            else:
                sum += A[i][j]
            if i == x-1:
                sum += A[i][j]
            if j == y-1:
                sum += A[i][j]
    return sum