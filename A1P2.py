import json
import csv
import pandas as pd
from matplotlib import pyplot as plt

with open("./layer0_paper.json") as file:
    data = json.load(file)
    

fname = "output.csv"


top10_dict = {}
pub_list = []
for content in data:
    temp = []
    
    author_str = ""
    for item in content["AA"]:
        author_str += (item["AuN"] + ";")


        if item["AuN"] in top10_dict:
            top10_dict[item["AuN"]] += 1

        else:
            top10_dict[item["AuN"]] = 1


    temp.append(" " + str(content["Id"]))
    temp.append(content["Ti"])
    temp.append(" " + content["D"])
    temp.append(author_str[:-1])
    pub_list.append(temp)
    

top10_list = sorted(top10_dict, key=top10_dict.get, reverse=True)[:10]

y = []
for author in top10_list:
    y.append(top10_dict[author])

plt.bar(top10_list, y)
plt.xticks(rotation = 50, fontsize=4)
plt.autoscale()
plt.show()


with open(fname, "w") as file:
    csv_file = csv.writer(file)
    

df = pd.DataFrame(pub_list, columns = ["paperID", "paper title", "publish years", "authors"])
df.to_csv('./output.csv', index=False)

