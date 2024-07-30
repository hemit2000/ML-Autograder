def matching_paren(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False 
            stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False

print(matching_paren("((()))"))
