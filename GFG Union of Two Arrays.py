class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        hashset = set()
        for i in range (0,n):
            hashset.add(a[i])
        for i in range (0,m):
            hashset.add(b[i])
        return len(hashset)