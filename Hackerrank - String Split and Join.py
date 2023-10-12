def split_and_join(line):
    # write your code here
    line_list = line.split(" ")
    new_line = "-".join(line_list)
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)