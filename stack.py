class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

def infix_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    postfix = ''
    
    for char in infix_expression:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while not stack.is_empty() and stack.peek() != '(' and precedence[char] <= precedence[stack.peek()]:
                postfix += stack.pop()
            stack.push(char)
    
    while not stack.is_empty():
        postfix += stack.pop()
    
    return postfix


infix_expression = "3+4*5"
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix expression:", postfix_expression)

infix_expression = "2*(3+4)"
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix expression:", postfix_expression)

