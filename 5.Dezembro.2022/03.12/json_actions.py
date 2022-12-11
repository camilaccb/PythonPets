from json import dumps
from json import loads

dict_contatos = {'Camila': 996662597, 'Joana': 987873590, 'Ismenia': 996179215}


json_file = "json_action.json"

with open(json_file, mode = "w", encoding= "utf-8") as f:
    json_string = dumps(dict_contatos, indent=1)            # Transforms dictionary to string
    f.write(json_string)

with open(json_file, mode= "r", encoding= "utf-8") as f:
    json_object = loads(f.read())                           # Transforms object to dictionary:
    print(json_object)

with open(json_file, mode = "w", encoding= "utf-8") as f:
    json_object['Mariana'] = 988472724
    json_string = dumps(json_object, indent=1)
    f.write(json_string)




