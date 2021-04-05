def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    diff_string = ''
    string_list = list(phrase)
    string_list.reverse()
    for letter in string_list:
        diff_string += letter
    if diff_string.lower() == phrase.lower():
        return True
    else:
        return False
