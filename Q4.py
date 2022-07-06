# Create functions that uses +,-,*,/
def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2
# Create dict that stores sign and function as key-value pairs
operations = {'+':add, '-':sub, '*':mul, '/':div}

def evaluate(expression):
    current_value = 0
    if '*' in expression:
        print(expression.split('*'))
        print('Hi')
#print(evaluate("1+2-3+4"))
print(evaluate("3.5+4*3.0/4-12/5+1.2"))

# LEFTOVER ISSUE: How to split string of expression based on operators(with precedence)