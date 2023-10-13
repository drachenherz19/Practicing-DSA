def countingValleys(steps, path):
    # Write your code here
    path = [-1 if i=="D" else 1 for i in path]
    level = 0
    valley = 0
    for i in path:
        level += i
        if i>0 and level==0:
            valley += 1
    return valley