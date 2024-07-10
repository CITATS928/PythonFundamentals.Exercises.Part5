def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    newvalue = value.replace(" ","").upper()
    reverse = newvalue[::-1]
    return newvalue==reverse

"""     for i in range(0,len(newvalue)):
        if(newvalue[0+i]!=newvalue[-1-i]):
            return False
        else:
            return True """
    #pass  # remove pass statement and implement me
