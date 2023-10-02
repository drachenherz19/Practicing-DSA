class Solution:
    #Function to fill the array elements into a hash table using Linear Probing to handle collisions.
    def insert(self,e,hashSize,table):
        h=e%hashSize
        i=h
        while table[i]!=-1:
            if table[i]==e:
                return
            i=(i+1)%hashSize
            if i==h:
                return
        table[i]=e
            
    def linearProbing(self,hashSize, arr, sizeOfArray):
        #Your code here
       table=[-1]*hashSize
       for e in arr:
           self.insert(e,hashSize,table)
       return table 