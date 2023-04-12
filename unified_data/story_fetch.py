import json
import csv
from pprint import pprint
out = {}

def convert_stories_before_1065_info_to_json():
    # Data Source: (Before 1065): 貓吧 (Name + Source)
    with open("doraep.csv",'r',encoding="UTF8") as f:
        rows = csv.reader(f)
        print(rows)
        for row in rows:
            out[row[0]] = [row[1],row[2]]
    with open("eps.json","w+") as f:
        f.write(json.dumps(out))
def convert_stories_after_1065_sources_to_json():
    # Data Source: (After 1065 (some mixed data before 1065)): Doraemon Wiki+Wikipedia (Source Only)
    with open("ddd.csv",'r',encoding="UTF8") as f:
        rows = csv.reader(f)
        print(rows)
        for row in rows:
            out[row[0]] = ["???",row[1]]
    with open("eps2.json","w+") as f:
        f.write(json.dumps(out))
def convert_merge_stories_info_to_json():
    # Open Previously Generated JSONs
    with open("eps.json","r") as f:
        datas = json.load(f)
    with open("eps2.json","r") as f:
        dt = json.load(f)
    # Data Source: (After 1065 (some mixed data before 1065)): Doraemon Wiki+Wikipedia (Name Only)
    with open("ddd2.csv",'r',encoding="UTF8") as f:
        rows = csv.reader(f)
        print(rows)
        for row in rows:
            try:
                dt[row[0]] = [row[1],dt[row[0]][1]]
            except:
                pass
        d2t = sorted(dt)
        dt = {key:dt[key] for key in d2t}
    # Merge sources as new JSON
    with open("eps.json","w") as f:
        for d in dt:
            if d not in datas:
                datas[d] = dt[d]

        json.dump(datas,f)

convert_stories_before_1065_info_to_json()
convert_stories_after_1065_sources_to_json()
convert_merge_stories_info_to_json()
"""
Functionality:
convert_stories_before_1065_info_to_json():
- Reads a CSV file called doraep.csv.
- Adds the story name and source from each row to the out dictionary.
- Dumps out to a JSON file called eps.json.

convert_stories_after_1065_sources_to_json():
- Reads a CSV file called ddd.csv.
- Adds the source from each row to the out dictionary. Story name is set to ???.
- Dumps out to a JSON file called eps2.json.

convert_merge_stories_info_to_json():
- Loads the previous JSON files eps.json and eps2.json.
- Reads a CSV file called ddd2.csv.
- Updates the story name in dt using the data from ddd2.csv.
- Merges the data from dt into datas, overwriting any duplicate keys.
- Dumps the merged data in datas to a JSON file called eps.json.
"""