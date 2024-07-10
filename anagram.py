def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    first_anagram = sorted(first_string)
    second_anagram = sorted(second_string)
    if(first_anagram==second_anagram):
        return True
    else:
        return False
