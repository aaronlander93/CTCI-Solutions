def palindrome_permutation(string):
    string = string.replace(' ', '')
    string_copy = list(string)
    count = 0
    
    if len(string) % 2 == 0:
        for letter in string_copy:
            if letter == 0:
                continue
            try:
                test = letter
                index = string_copy.index(test)
                string_copy[index] = 0
                index = string_copy.index(test)
                string_copy[index] = 0
            except:
                return False
        return True

    if len(string) % 2 != 0:
        pivot_char = 0
        for letter in string_copy:
            if letter == 0:
                continue
            try:
                test = letter
                index = string_copy.index(test)
                string_copy[index] = 0
                index = string_copy.index(test)
                string_copy[index] = 0
            except:
                pivot_char += 1

                if pivot_char > 1:
                    return False
        return True

                
                
