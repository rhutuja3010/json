import json 
dic={"emp1":{"name":"lisa","design":"programmer","age":"34","salary":"54000"},
            "emp2":{"name":"Elis","design":"trainee","age":24,"salory":"40000"},
}
out_file=open("my_file.json","w")
json.dump(dic,out_file,indent=4)
out_file=close()