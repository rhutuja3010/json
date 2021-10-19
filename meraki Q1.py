# Q.1 Json data ko python object main convert karne ka program likho?. Example: Input :- Output :

import json

x='{"a":"sinu","b":"sffhj","c":"frjkjs","d":"wqiugd"}'
# a=json.loads(x)
# print(type(a))
# print(a)

a=open("question6.json","w")
json.loads(x,a,indent=4)
a.close()
    
# with open("question1.json","r") as f:
#     y=json.load(f)
#     print(y)


# # x='{"a":"sinu","b":"sffhj","c":"frjkjs","d":"wqiugd"}'
# y=json.loads(x)
# # print(y)
# for i in y:
#     print(i,y[i])