import csv

def add_quotes(string:str) -> str:
    return '"' + string + '"'

def write_human(entity:str, name:str, city:str, phone:int):
    with open('./humans.csv', 'a', encoding='UTF8', newline='') as humans:
        writer = csv.writer(humans, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow([entity, name, city, phone])