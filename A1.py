import pandas as pd
from matplotlib import pyplot as plt



#function used for converting YYYY-MM to MM/YYYY
def format_str(list):
    
    for i in range(len(list)):
        list[i] = "%s/%s"%(list[i][5:7], list[i][0:4])



#read CSV
df = pd.read_csv('crypto_github_events.csv')

#find top 10 users
users = df['userID']

#dictionary containing <user>:<github actions count>
top10_dict = {}

for user in users:
    if user in top10_dict:
        top10_dict[user] +=1
    else:
        top10_dict[user] = 1


top10_list = sorted(top10_dict, key=top10_dict.get, reverse=True)[0:10]



#dictionary containing <user>:{<month>:<monthly actions>}
total_dict = {}
top5_dict = {}


#find monthly actions
for user in top10_list:
    
    month_dict = {}
    Date = df[(df['userID']) == user]['date'].to_string(index=False)

    list = Date.split("\n")
    list = sorted(list)
    format_str(list)

    curr_month = " " + list[0][0:7]
    count =0
    
    for item in list:
        
        month = " " + item[0:7]
        
        if month == curr_month:
            count +=1

        else:
            month_dict[curr_month] = count
            curr_month = " " + item[0:7]
            count = 1

        if item == list[len(list)-1]:
            month_dict[curr_month] = count

    total_dict[" " + user] = month_dict


#plotting top 5 users and outputting excel sheet
user_count = 0
x = []
y = []

plt.figure(figsize=(12,5))

for user in total_dict:

    if user_count < 5:

        user_count +=1

        for date in total_dict[user]:
            
            year = date[4:8]

            if year == "2016":
                x.append(date)
                y.append(total_dict[user][date])

        
        line = plt.plot(x,y)
        plt.text(x[0], y[0], user, color=line[0].get_color())
        plt.autoscale()
        x = []
        y = []

df_out = pd.DataFrame(data=total_dict).transpose()
df_out.to_csv('data.csv', index_label='User ID')

plt.plot(x,y)
plt.show()





