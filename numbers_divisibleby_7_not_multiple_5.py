'''
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

def valid_numbers(start_num,end_num):
    valid_number_list = []
    for number in range(start_num,end_num):
        if ((number % 7 == 0) & (number/5 !=0)):
            valid_number_list.append(str(number))
    #print (valid_number_list)
    return (','.join(valid_number_list))

start_num=2000
end_num=3201
print (valid_numbers(start_num,end_num))



