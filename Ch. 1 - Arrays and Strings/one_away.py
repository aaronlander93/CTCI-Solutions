def one_away(str1, str2):
    common_char = 0
    small_hash = {}

    #Find the bigger string
    if len(str1) >= len(str2):
        big_string, small_string = str1, str2
    else:
        big, small = str2, str1

    #Convert smaller string into hash map
    for letter in small:
        small_hash[letter] = 1
        
    #Iterate through big string    
    for letter in big:
        #Test if letter is in small string
        try:
            test = small_hash[letter]
            common_char += 1
        except:
            continue

    #There should be len(big)-1 commonalities if it is one away
    if common_char == len(big)-1:
        return True
    else:
        return False

