def find_avg(name, student_marks):
    for key in student_marks:
        if key == name:
            records = student_marks[key]
            import statistics
            average = statistics.mean(records)
            return average
    
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    avg = find_avg(query_name, student_marks)
    print('%.2f' % avg)