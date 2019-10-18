import bs4
import requests
import json
import csv

IDs = []
with open('../Testcases/Test/ID.csv','r') as file:
    line = file.readline()
    while line:
          IDs.append(line[:-1])
          line = file.readline()
IDs = IDs[1:]


with open('../CSV Files/output.csv','w') as file:
        file.write("ID,Joke\n")
for i in range(len(IDs)):
    url = "http://api.icndb.com/jokes/" + IDs[i]
    print(url)
    response = requests.get(url)
    response_dict = json.loads(response.content)
    joke = response_dict["value"]["joke"]

    with open('../CSV Files/output.csv','a') as file: # 'a' for append
        fieldnames = ['ID' , 'Joke']
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writerow({'ID' : IDs[i], 'Joke' : joke})

