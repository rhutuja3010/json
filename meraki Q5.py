
# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?import json
import json
def complexnumber(object):
    if 'complex' in object:
        return complex(object['real'],object['img'])
    return object
complex_object=json.loads('{"complex":true,"real":5,"img":2}',object_hook=complexnumber)
simple_object=json.loads('{"real":5,"img":2}',object_hook=complexnumber)
print("complex_object:",complex_object)
print("without complexobject",simple_object)

# d={"key":1,"sab":2,"fds":3}

# with open("myfile1.json","w") as f:
#     json.dump(f,d,indent=4)
  
    