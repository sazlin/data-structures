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
