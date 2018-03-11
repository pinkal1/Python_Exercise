
# Program which opens up file and displays sum of all numbers

'''with open('C:\Users\Jay\Desktop\InterviewPreparatioPython\sample.txt','r+') as my_file:
 #print my_file.readline()
 sum=0
 for f in my_file:
     sum=sum+int(f)
 print ("Total is",sum)

my_file.close()'''

#using generator
print sum(int(contents.strip())for contents in open('C:\Users\Jay\Desktop\InterviewPreparatioPython\sample.txt','r+'))