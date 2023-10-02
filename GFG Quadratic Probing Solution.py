class Solution:
    
    #Function to fill the array elements into a hash table using Quadratic Probing to handle collisions.
    def QuadraticProbing(self,hash, hashSize, arr, N):
        # ht = [-1] * hashSize
        for each in arr:
            if each in hash:
                continue
            r = each % hashSize
            if hash[r] == -1:
                hash[r] = each
            else:
                ct = 0
                while ct < hashSize:
                    r = (each + (ct+1)**2) % hashSize
                    if hash[r] == -1:
                        hash[r] = each
                        break
                    ct +=1