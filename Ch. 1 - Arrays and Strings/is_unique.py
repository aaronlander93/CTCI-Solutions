def is_unique(string):
    string_hash = {}
    
    for letter in string:
        try:
            test = string_hash[letter]
            return False
        except:
            string_hash[letter] = 1
    return True
