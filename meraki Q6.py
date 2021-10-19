# Q6.Python object key unique key value ko access karne ka program likho?
import json
list1=[2,4,7,1,9,3]
list2=[4,7,1,4,9,0,3,5,6]
for i in list2:
    if i not in list1:
        print(i)
