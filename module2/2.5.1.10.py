text1 = input('Enter text 1: ').lower()
text2 = input('Enter text 2: ').lower()

current_index = 0

for character in text1:
    current_index = text2.find(character, current_index)
    
    if -1 == current_index:
        break

if -1 == current_index:
    print('No')
else:
    print('Yes')