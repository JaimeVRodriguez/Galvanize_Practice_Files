def fizz_buzz():
    '''Returns the numbers from 1 to 100 into list. But for
    multiples of three append "Fizz" instead of the number and for the multiples
    of five append "Buzz". For numbers which are multiples of both three and five
    append "FizzBuzz".

    The first five elements of the output list are:
        lst = [1, 2, "Fizz", 4, "Buzz", ....]

    Parameters
    ----------
    None

    Returns
    -------
    list
    '''
    lst = []
    for i in range(1, 101):
        if i % 15 == 0:
            lst.append("FizzBuzz")
        elif i % 5 == 0:
            lst.append("Buzz")
        elif i % 3 == 0:
            lst.append("Fizz")
        else:
            lst.append(i)

    return lst


def count_characters(string):
    '''
    Return a dictionary which contains
    a count of the number of times each character appears in the string.
    Characters which with a count of 0 should not be included in the
    output dictionary.


    Parameters
    ----------
    string: str

    Returns
    -------
    dict
        A dictionary with counts of each character in string
    '''

    letter_count_dict = {}

    for letter in string:
        if letter in letter_count_dict:
            letter_count_dict[letter] += 1
        else:
            letter_count_dict[letter] = 1

    return letter_count_dict


print(count_characters(
    "this is a test a test for a string and the function that count count words a is"))
