from stack import Stack
from stack import EmptyStackError


def check_parens(str):
    """
    check_parens takes a string and:
    returns 0 if the number of parentheses is balanced and matched.
    returns 1 if more left parentheses than right.
    returns -1 if string has broken (unmatched) parentheses.
    """

    stack = Stack()
    for i in range(len(str)):
        # if loop encounters (, location is pushed to stack.
        if str[i] == '(':
            stack.push(i)
        # else if loop encounters ), attempt to pop from stack. If stack is
        # empty, catch EmptyStackError and return -1. We have seen too many ).
        elif str[i] == ')':
            try:
                stack.pop()
            except EmptyStackError:
                return -1
    # after going through str looking for parentheses, if there is anything
    # left on the stack, we have too many (, but if we catch an EmptyStackError
    # we know the parentheses were balanced.
    try:
        stack.pop()
        return 1
    except EmptyStackError:
        return 0
'''
def check_parens(str):
    """
    This function meets the requirements given, but it is clearly inadequate
    for some invalid strings, such as ')('.
    """
    counter = str.count('(') - str.count(')')
    if counter > 0:
        return 1
    elif counter == 0:
        return 0
    else:
        return -1
'''
