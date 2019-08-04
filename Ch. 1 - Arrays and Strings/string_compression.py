def compress_string(string):
    comp_char = string[0]
    compressed_string = ''
    repeat_count = 0
    
    for letter in string:
        if letter != comp_char:
            compressed_string += comp_char + str(repeat_count)
            comp_char = letter
            repeat_count = 1
        else:
            repeat_count += 1
            
    compressed_string += comp_char + str(repeat_count)
    
    if len(compressed_string) >= len(string):
        return string
    else:
        return compressed_string

        
        
    
