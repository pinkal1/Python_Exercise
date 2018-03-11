#Given an array of integers, every element appears twice except for one. Find that single one.



'''

def singleNumber(nums):
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
        #return no_duplicate_list

nums=[1,2,4,3,1,5,8,2]
print singleNumber(nums)

'''



def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

nums=[1,2,4,3,1,5,8,2,1]
print singleNumber(nums)



