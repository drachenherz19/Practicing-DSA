lists=[]
for i in range(x+1):
    for j in range (y+1):
        for k in range (z+1):
            if i+j+k != n:
                list_list=[i,j,k]
                lists.append(list_list)

print(lists,end='')