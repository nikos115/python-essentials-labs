def encrypt(text, shift_value):
    cipher = ''
    code_Z = ord('Z')
    code_z = ord('z')
    cap_diff = ord('A') - code_Z - 1
    low_diff = ord('a') - code_z - 1
    
    for char in text:
        if not char.isalpha():
            cipher += char
        else:
            code_char = ord(char)
            code = code_char + shift_value
            
            if code_char <= code_Z and code > code_Z:
                code += cap_diff
            elif code > code_z:
                code += low_diff
                
            cipher += chr(code)
    
    return cipher


text = input('Enter your message: ')
shift_value = int(input('Enter a shift value from the range [1, 25]: '))
if shift_value not in range(26):
    print('Out of valid range')
else:
    print(encrypt(text, shift_value))
