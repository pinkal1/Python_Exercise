


'''
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

'''

import sys
net_amount = 0
while True:
    log=raw_input()
    if not log:
        break
    values = log.split(' ')
    operation = values[0]
    if operation == 'D':
        net_amount += int(values[1])
    elif  operation == 'W':
        net_amount -= int(values[1])
print net_amount
