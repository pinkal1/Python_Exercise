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

print (first_last([2,5,7,11,11,11,11,13,17,17,19, 20], 11)) #--> (4, 8)
print (first_last([1,2,2,3,4,4,4,4,4,5,5,6,7,8], 6)) #--> (11, 11)


def first_last(list, seach_element):
	l=[]
	for ele in list:
		if ele == seach_element:
			curr_ele_index=list.index(ele)
			l.append(curr_ele_index)
			for x in range(curr_ele_index,len(list)):
				if list[x] == list[x+1]:
					curr_ele_index=curr_ele_index+1
				else:
					break
			break
	l.append(curr_ele_index)
	return l


print (first_last([2,5,7,11,11,11,11,13,17,17,19, 20], 11)) #--> (3, 6)
print (first_last([1,2,2,3,4,4,4,4,4,5,5,6,7,8], 6)) #--> (11, 11)