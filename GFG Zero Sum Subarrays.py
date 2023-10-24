class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        summ1=0
        count=0
        hashMap = {}
        out = []
        for i in range(0,n):
            summ1 = summ1 + arr[i]
            if summ1 ==0:
                out.append((0,i))
                count +=1
            al = []
            
            if summ1 in hashMap:
                al = hashMap.get(summ1)
                for x in range(len(al)):
                    out.append((al[x] +1, i))
                    count+=1
            al.append(i)
            hashMap[summ1]=al
        return count