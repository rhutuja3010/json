# Q.2 Python object ko json data main convert karne ka program likho? Example: Input :- Output:-

import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
# abc_file=open("question2.json","w")
# json.dump(x,abc_file,indent=4)
# abc_file.close()

