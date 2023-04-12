from flask import Flask, render_template, flash, redirect, url_for, Markup, request
import json
import re
import time
app = Flask(__name__)
app.secret_key = 'your_secret_key'
# Types: 01= DR()BDSP, 02 = BDSP, 03= NOR, 04 = MV, 05 = General sp
with open("ntv.json", "r", encoding="UTF8") as f:
    tvs = json.load(f)


def search(query):
    global tvs
    data = tvs
    start_time = time.time()
    keywords = re.findall(r'\w+', query.lower())
    results = []
    output = []
    for year, episodes in data.items():
        for item in episodes:
            count = sum(1 for keyword in keywords if keyword in " ".join(item["keywords"]) or any(
                keyword in s for s in item["storyName"]) or any(keyword in s for s in item["isRemake"] if s is not False) or (keyword == item["Episode"]))
            if count > 0:
                results.append({"year": year, "item": item, "count": count})

    results.sort(key=lambda x: x["count"], reverse=True)

    for result in results:
        year = result["year"]
        item = result["item"]
        count = result["count"]
        output.append([year, item['Episode'], [keyword for keyword in keywords if (keyword in ' '.join(item['keywords'])) or any(keyword in s for s in item['storyName']) or any(
            keyword in s for s in item['isRemake'] if s is not False) or (keyword == item['Episode'])], item['storyName'], item['isRemake'], item['keywords'], count])
    end_time = time.time()
    elapsed_time = end_time - start_time
    return f"{elapsed_time:.3f}", output


@app.route('/')
def index():
    #flash('Hello, World!')
    return render_template('list.html', mov=tvs)


@app.route('/search')
def searchui():
    query = request.args.get('query')
    if query != None:
        return render_template("search.html", query=query, result=search(query))
    else:
        return redirect(url_for("index"))


@app.route('/play/<year>/<ep>')
def play(year, ep):
    for e in tvs[year]:
        if ep == e["Episode"]:
            return render_template("play.html", episode=e["Episode"], year=year, epvid=e["filename"], story=e["storyName"], remake=e["isRemake"], desc=e["keywords"])

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
