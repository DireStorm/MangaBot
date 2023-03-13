import json
import datetime as dt

curr_date = str(dt.date.today())

with open("data.json") as f:
    data = json.load(f)
    
# for date in data:
#     if(date["date"] == curr_date):
#         for entry in date["entries"]:
#             print("\t", entry)


#Modifying data
for date in data:
    if(date["date"] == curr_date):
        date["entries"].append("whatever additional todo")
        break
else:
    add_dict = {}
    add_dict["date"] = curr_date 
    add_dict["entries"] = []
    add_dict["entries"].append("whatever additional todo")
    data.append(add_dict)
    
#Overwrite Data
with open("data.json", "w") as f:
    json.dump(data, f)