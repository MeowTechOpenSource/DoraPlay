import requests
import json
from bs4 import BeautifulSoup
ep = {}
# This script downloads the data from ChineseDora, some episodes are missing 1192,1259 are missing due to some formatting error, please find it by yourself.
# Due to copyright issues, we do not provide the information.
for n in range(1,1286):
    # Make a GET request to the webpage
    url = f'https://chinesedora.com/database/{n}.htm'
    print("Fetching Episode:",n,url)
    response = requests.get(url)
    try:
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the container with class "lefttable"
        lefttable = soup.find('div', {'class': 'lefttable'})
        # Get all <p> elements before the first <div> with class "df21539aee8b7903a86891e269ef67a7"
        p_tags = []
        for tag in lefttable.find_all(['p'], recursive=True):
            if tag.name == 'div' and 'class' in tag.attrs and 'df21539aee8b7903a86891e269ef67a7' in tag.attrs['class']:
                break
            if tag.name == 'p':
                for img in tag.find_all('img'):
                    img.decompose()  # Remove the <img> tag
                p_tags.append(tag)
                print(tag.text)

        # Print out the results
        ep[str(n)] = ""
        for p in p_tags:
            ep[str(n)] = ep[str(n)] + p.text
    except:
        pass
# The out.json will include all the episode details encoded in UTF-8.
with open("out.json","w",encoding="UTF8") as f:
    json.dump(ep,f)
"""
Functionality:
- Loops through episode numbers from 1 to 1286.
- Requests the HTML for each episode page.
- Parses the HTML into a BeautifulSoup object.
- Gets the lefttable div and p_tags containing the description.
- Removes any img tags from the p_tags.
- Adds the description text from the p_tags to the ep dictionary.
- Dumps the ep dictionary to a JSON file called out.json.
"""