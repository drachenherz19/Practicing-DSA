def getMoneySpent(keyboards, drives, b):
    max_spent = -1
    
    for i in keyboards:
        for j in drives:
            total_cost = i + j
            if total_cost <= b and total_cost > max_spent:
                max_spent = total_cost
    
    return max_spent