str_list = list(input('Enter birthday (YYYYMMDD): '))
num_list = [int(i) for i in str_list] # sum() takes numbers not strings
tmp_sum = 0

while len(num_list) > 1:
    tmp_sum = sum(num_list)
    num_list = [int(i) for i in str(tmp_sum)]
    
print(tmp_sum)