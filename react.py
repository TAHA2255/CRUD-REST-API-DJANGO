import requests
import json
URL = 'http://127.0.0.1:8000/studentapi/'


def get(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    d = json.dumps(data)
    r = requests.get(url=URL, data=d)
    j = r.json()
    print(j)
def create():
    data = {"name": "anwar", "school": "SMI UNIVERSITY", "age": 30}
    d = json.dumps(data)
    r = requests.post(url=URL, data=d)
    j = r.json()
    print(j)
def update():
    data = {"id": 2, "name": "arshad", "school": "SIR SYED UNIVERSITY"}
    d = json.dumps(data)
    r = requests.put(url=URL, data=d)
    j = r.json()
    print(j)
def delete(id):
    data = {'id': id}
    d = json.dumps(data)
    r = requests.delete(url=URL, data=d)
    j = r.json()
    print(j)

# get(3)
# create()
# update()
# delete(3)