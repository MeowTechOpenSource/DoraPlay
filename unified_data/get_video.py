import os
import json
import re
tvs = {}
episodesx = 739
ce = 0
for year in range(2005,2023):
    tvs[str(year)] = []
    episodes = os.listdir(f"./{str(year)}/")
    ce = 0
    for i in range(1,episodesx+1):
        print(year, ce)
        ce+=1
        found = False
        for ep in episodes:
            if "{:03d}".format(ce) in ep.replace(str(year),"").replace("X264","").replace("1080","").replace("480p",""):
                firm = "UNKNOWN"
                if "[YGSUB]" in ep:
                    firm = "YGSUB"
                elif "[钉铛字幕组]" in ep:
                    firm = "DINGDONGSUB"
                elif "[DORASUB]" in ep:
                    firm = "DORASUB"
                elif "[夜莺家族]" in ep:
                    firm = "NIGHTFAM"
                elif "[梦蓝字幕组]" in ep:
                    firm = "MLSUB"
                tvs[str(year)].append({"Episode":"{:03d}".format(ce),"storyName":"{Soon}","isRemake":False,"remakeTimes":0,"Type":"00", "SubFirm":firm, "Gadgets":[], "keywords":[],"filename":ep})
                break
with open("tv.json","w",encoding="UTF-8") as f:
    f.write(json.dumps(tvs))
"""
Functionality:
- Loops through years from 2005 to 2022.
- Gets the list of episode video files for each year.
- Loops through episode numbers from 1 to episodesx.
- Searches the episode video files for the current episode number.
- When a match is found, extracts the subtitle group and adds the episode details to the tvs dictionary.
- Dumps the tvs dictionary to a JSON file called tv.json.
"""