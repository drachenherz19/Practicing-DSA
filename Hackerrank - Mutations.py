def mutate_string(string, position, character):
    
    #convert the string to a list to make it mutable
    string_list = list(string)
    
    #update the character at the specified position
    string_list[position] = character
    
    #join the list back into a string 
    mutated_string = ''.join(string_list)
    
    return mutated_string