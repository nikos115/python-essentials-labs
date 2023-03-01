text1_list = list(input('Enter text 1: ').lower())
text2_list = list(input('Enter text 2: ').lower())

# empty strings cannot be anagrams
# nor strings with different length

if not len(text1_list) or len(text1_list) != len(text2_list):
    print('Not anagrams')
else:
    # remove each character of text1 from text2
    # in the end text2 should be empty
    
    for character in text1_list:
        if character in text2_list:
            text2_list.remove(character)
        else:
            break
        
    if len(text2_list):
        print('Not anagrams')
    else:
        print('Anagrams')
        
    