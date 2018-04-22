#!/usr/bin/python

json_dataR={"first_name": "James", "last_name": "Bond"}
json_dataW={"first_name": "James", "last_name": "Bond", "age": 23}
import json
from app import *

#zadanie 2
print('test zadania 2')
print('zwroc dobry wynik: ')
result=process_json(json.dumps(json_dataR))
print(result)
print('zwroc zly wynik: ')
result=process_json(json.dumps(json_dataW))
print(result)
