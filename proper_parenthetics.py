def check_parens(str):
    """
    check_parens takes a string and:
    returns 0 if the number of parentheses is balanced and matched.
    returns 1 if more left parentheses than right.
    returns -1 if string has broken (unmatched) parentheses.
    """

    counter = 0
    for i in range(len(str)):
        # if loop encounters (, counter is incremented
        if str[i] == '(':
            counter += 1
        # else if loop encounters ), decrement counter
        elif str[i] == ')':
            if counter == 0:
                return -1
            else:
                counter -= 1
    # after going through str looking for parentheses, if counter still
    # positive, we have too many (, but if counter 0 we have balanced parens.
    if counter > 0:
        return 1
    elif counter == 0:
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
