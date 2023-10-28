n = int(input())
N = set(map(int, input().split()))

m = int(input())
M = set(map(int, input().split()))


print(len(M.union(N))