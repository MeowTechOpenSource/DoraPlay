import json
import csv
out = {}
# Open the previously generated story name and sources list
with open("eps.json","r",encoding="UTF8") as f:
    m = json.load(f)
# Data Source: 貓吧+Wikipedia+Doraemon Wiki
# Create a dictionary including story no. which each episode includes (e.g 1->1,2,3)
with open("main.csv","r",encoding="UTF8") as f:
    rows = csv.reader(f)
    for row in rows:
        if row[0].replace("\ufeff", "") not in out:
            out[row[0].replace("\ufeff", "")] = []
        out[row[0].replace("\ufeff", "")].append(row[1])
# Write the dictionary as JSON for later use
with open("episodec.json","w") as f:
    json.dump(out,f)
"""
Functionality:
- Loads the story name and source data from eps.json.
- Reads a CSV file called main.csv.
- For each row, adds the story number to a list for the corresponding episode number key in out.
- Dumps the out dictionary to a JSON file called episodec.json.
"""