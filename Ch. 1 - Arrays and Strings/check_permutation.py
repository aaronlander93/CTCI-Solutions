def check_permutation(string):
    string = string.replace(' ', '')

    string_forward = list(string)
    string_backward = list(reversed(string))

    for i in range(0, len(string)):
        if string_forward[i] == string_backward[i]:
            continue
        else:
            return False
    return True
