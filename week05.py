def check_parentheses(expression):
    stack = []
    brackets = {')' : '(', ']' : '[', '}' : '{'}
    for letter in expression :
        if letter in brackets.values():
            stack.append(letter)
        if letter in brackets.keys():
            if not stack or stack.pop() != brackets[letter] :
                return False
    return not stack

print(check_parentheses("[2*{34+5}-15+(1+9)])"))