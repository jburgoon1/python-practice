def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    complete_str =''
    temp_list = list(phrase)
    temp_list.reverse()
    for string in temp_list:
        complete_str+=string
    return complete_str
    
