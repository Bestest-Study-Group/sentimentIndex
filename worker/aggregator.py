import http.client
import json
from textblob import TextBlob

def main():
    conn = http.client.HTTPSConnection("free-news.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Host': "free-news.p.rapidapi.com",
        'X-RapidAPI-Key': "1c08d74bdcmsheabc554769b54f1p1455d2jsn6f0e0abf2ded"
        }

    conn.request("GET", "/v1/search?q=stock%20market&lang=en&page=1", headers=headers)

    res = conn.getresponse()
    data = res.read()

    articles = json.loads(data)["articles"]

    sum = 0.0

    print("[")

    for article in articles:
        if (article["summary"] == None):
            blob = TextBlob(article["title"])
            article["summary"] = "No Article"
        else:
            blob = TextBlob(article["summary"])
        senti = blob.sentiment.polarity
        sum += senti
        print("Example(\"" + article["title"] + "\", \"\"),")

    print("]")
    
    #print("OVERALL SENTIMENT: " + str(sum/len(articles)*5))

if __name__ == "__main__":
    main()