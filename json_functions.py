import json

def get_tokens_records():                               # Récupère les donées de json les transforme en dict python
    json_file = open("tokens_amount_value.json", "r")
    json_data = json_file.read()
    json_file.close()
    tokens = json.loads(json_data)
    return tokens

def alter_tokens_records(token_dict):                   # Prend en paramètre un dictionnaire Python, le convertit en fichier json et réecrit le ficher
    json_data = json.dumps(token_dict)
    json_file = open("tokens_amount_value.json", "w")
    json_file.write(json_data)
    json_file.close()
 

