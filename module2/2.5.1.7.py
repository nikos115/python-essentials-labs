text = input("Enter text to check: ")

lower_text = ''.join(text.split()).lower()

if lower_text and lower_text == lower_text[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")