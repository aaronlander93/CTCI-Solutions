def urlify(string):
    url = ''
    
    for letter in string:
        if letter == ' ':
            url += '%20'
        else:
            url += letter
    return url


            
