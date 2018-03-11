'''def findUniqieChar(str):
    uniqueList=[]
    for i in str:
        if i not in uniqueList:
            uniqueList.append(i)
        else:
            return False
    return True


str='pinkalapo'
print findUniqieChar(str)

'''

'''
def findUniqieChar(str):
    uniqueList={}
    for i in str:
        if i not in uniqueList.keys():
            uniqueList[i]=1
        else:
            uniqueList[i] += 1
    #return uniqueList

    for k, v in uniqueList.items():
        if v == 1:
            print k

str='pinkalapo'
#print findUniqieChar(str)
findUniqieChar(str)

'''

# O(N)
import unittest


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abacd'), ('s4afad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()