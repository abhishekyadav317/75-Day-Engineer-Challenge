# Valid Parenthesis (medium)

stack = []

brackets = '()[]{})('

matching = {
    ')' : '(',
    ']' : '[',
    '}' : '{'
}

for bracket in brackets :
    
    # if bracket in "([{"
    if bracket == '('  or bracket =='[' or bracket == '{' :
        stack.append(bracket)
        

    if bracket == ')' or bracket == ']' or bracket == '}':
        if stack == [] :
            print(False)
            
            
        else :
            if stack[-1] == matching[bracket] :
                stack.pop()
                
                
            else :
                print(False)
                break

if stack == [] :
    print(True)
else:
    print(False)

            




