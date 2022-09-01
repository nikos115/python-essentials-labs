leds = [['###', '  #', '###', '###', '# #', '###', '###', '###', '###', '###'],
        ['# #', '  #', '  #', '  #', '# #', '#  ', '#  ', '  #', '# #', '# #'],
        ['# #', '  #', '###', '###', '###', '###', '###', '  #', '###', '###'],
        ['# #', '  #', '#  ', '  #', '  #', '  #', '# #', '  #', '# #', '  #'],
        ['###', '  #', '###', '###', '  #', '###', '###', '  #', '###', '###']]

rows = [[], [], [], [], []] # led output

number = input('enter any positive integer:')

# validate each input character to be int
# append each character leds to output rows

for n in number:
    if n.isdigit():
        i = int(n)
        for r in range(5):
            rows[r].append(leds[r][i])    
    else:
        rows = [['wrong input']]
        break

# output each row
for row in rows:
    print(' '.join(row))