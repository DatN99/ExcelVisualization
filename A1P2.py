import json
import csv

with open("./layer0_paper.json") as file:
    data = json.load(file)
    

fname = "output.csv"


'''
with open(fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow([])
'''

json_list = []
for content in data:
    temp = []
    
    author_list = []
    for item in content["AA"]:
        author_list.append(item["AuN"])

    temp.append(author_list)
    temp.append(content["Ti"])
    temp.append(content["D"])
    temp.append(content["Id"])


    json_list.append(temp)
    

print(json_list)

'''
        for item in content["AA"]:

            print(item)
            csv_file.writerow([item['AuId']])
'''