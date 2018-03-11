#2,5,7,11,11,11,11,13,17,17,19, 20
#param:11
#output: 3, 6


def first_last(list, num):
	first, last = -1,-1

	for i, x in enumerate(list):
		#print str(x) + "  " + str(num)
		if (first == -1 and x == num):
			first = i
		if (first != -1 and x != num):
			last = i - 1
			break

	return first, last

print first_last([2,5,7,11,11,11,11,13,17,17,19, 20], 11) #--> (4, 8)
print first_last([1,2,2,3,4,4,4,4,4,5,5,6,7,8], 6) #--> (11, 11)