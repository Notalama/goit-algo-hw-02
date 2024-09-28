def check_delimiters(s):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs.keys():
            if stack == [] or matching_pairs[char] != stack.pop():
                return "Несиметрично"
    
    if stack == []:
        return "Симетрично"
    else:
        return "Несиметрично"
    
print(check_delimiters("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(check_delimiters("( 23 ( 2 - 3);"))  # Несиметрично
print(check_delimiters("( 11 )"))  # Несиметрично
