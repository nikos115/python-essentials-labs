def read_int(prompt, min, max):
    try:
        i = int(input(prompt))
        assert min <= i <= max
        return i
    except ValueError:
        print('Error: wrong input')
    except AssertionError:
        print('Error: the value is not within the permitted range')
    
    # if we reach this point an exception has been raised
    # repeat yourself
    return read_int(prompt, min, max)    

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
