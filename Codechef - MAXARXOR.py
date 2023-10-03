import io, os, sys, math
from io import BytesIO, IOBase

#FASTIO
input = sys.stdin.readline
for _ in range (int(input())):
    n, k = map (int, input() .split())
    word = "1" *n
    x = int (word, 2)
    if k > (2**n)//2:
        k = (2**n)//2
   
    print (k*x*2)