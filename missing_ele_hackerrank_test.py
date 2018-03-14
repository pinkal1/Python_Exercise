
'''


def check_all_numbers(output):
    for element in output:
        if not isinstance(element,int):
            if not isinstance(element, tuple):
                return False
            else:
                if len(element) !=2:
                    return False
                (x,y)=element
                if not isinstance(x,int) or not isinstance(y,int):
                    return False
    return True
output=[1,4,5,3,(1,4)]
#output=['a',4,5,3,(1,4)]  # will be False
print check_all_numbers(output)

print "-----------------"

def no_consecutive_num(output):
    no_tuple_list=[element for element in output if not isinstance(element,tuple)]
    no_tuple_list=sorted(no_tuple_list)    #[1, 2, 5, 7]
    prev_num = None
    for element in no_tuple_list:
        if prev_num is not None and (element - prev_num) == 1:
            return False
        else:
            prev_num = element
    return  True

#output=[1,2,5,7,(6,9)]   # will be false
output=[1,4,5,3,(1,4)]
print no_consecutive_num(output)

'''


def tuples_intersect(t1, t2):
    min_t1, max_t1=t1
    min_t2,max_t2=t2
    if not (min_t1 < max_t1 and min_t2 < max_t2 and   max_t1 <min_t2):
       return  True
t1=(1,4)
t2=(4,10)
print tuples_intersect(t1, t2)    #(1,4),(3,10) True as it its intersecting   (1,4),(6,10) None
print "-----------------"



def no_overlap_tuples(output):
    tuple_only=[element for element in output if isinstance(element,tuple)]
    for i in range(len(tuple_only)):
        for j in range(len(tuple_only)):
            if(j > i):
                if tuples_intersect(tuple_only[i], tuple_only[j]):
                    return False
    return True

#output=[1,4,5,3,(1,4),(6,10)]
output=[1,4,5,3,(1,4),(5,10),(13,17)]
print no_overlap_tuples(output)

