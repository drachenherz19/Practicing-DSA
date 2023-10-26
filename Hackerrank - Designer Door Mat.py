N, M = map(int, input().split())

pattern = ".|."
for i in range(1, N, 2):
    print((i * pattern).center(M, "-"))

print("WELCOME".center(M, "-"))

for i in range(N - 2, 0, -2):
    print((i * pattern).center(M, "-"))