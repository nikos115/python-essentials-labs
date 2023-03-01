def mysplit(strng):
    strng = strng.strip()
    start = 0
    end = strng.find(' ')
    ret = []
    while end >= 0:
        if end > start:
            ret.append(strng[start:end])
        start = end + 1
        end = strng.find(' ', start)
    if start < len(strng):
       ret.append(strng[start:])
    return ret
    #
    # put your code here
    #


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
