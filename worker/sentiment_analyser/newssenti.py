import http.client
import json
import cohere
from cohere.classify import Example
from dotenv import load_dotenv
import os
from datetime import datetime

colin = [
Example("MSCI Inc. stock rises Wednesday, still underperforms market", "negative"),
Example("DraftKings Inc. stock rises Wednesday, outperforms market", "positive"),
Example("Willis Towers Watson PLC stock falls Tuesday, still outperforms market", "positive"),
Example("ONEOK Inc. stock rises Tuesday, outperforms market", "positive"),
Example("Marathon Oil Corp. stock falls Tuesday, still outperforms market", "positive"),
Example("Intuitive Surgical Inc. stock falls Tuesday, underperforms market", "positive"),
Example("Kohl's Corp. stock falls Monday, underperforms market", "negative"),
Example("Intuit Inc. stock rises Monday, still underperforms market", "negative"),
Example("Dow Inc. stock falls Monday, underperforms market", "negative"),
Example("Walgreens Boots Alliance Inc. stock rises Thursday, still underperforms market", "negative"),
Example("Waste Management Inc. stock rises Thursday, still underperforms market", "negative"),
Example("Teleflex Inc. stock rises Thursday, still underperforms market", "negative"),
Example("Public Storage stock rises Thursday, still underperforms market", "negative"),
Example("Kohl's Corp. stock rises Thursday, outperforms market", "positive"),
Example("Johnson Controls International PLC stock rises Thursday, outperforms market", "positive"),
Example("Regency Centers Corp. stock rises Friday, outperforms market", "positive"),
Example("Snap-On Inc. stock rises Friday, still underperforms market", "negative"),
Example("Cooper Cos. stock rises Friday, still underperforms market", "negative"),
Example("Unum Group stock rises Wednesday, still underperforms market", "negative"),
Example("United Rentals Inc. stock rises Wednesday, outperforms market", "positive"),
Example("Target Corp. stock outperforms market on strong trading day", "positive"),
Example("Snap Inc. stock rises Wednesday, outperforms market", "positive"),
Example("Paramount Global Cl B stock outperforms market on strong trading day", "positive"),
Example("Live Nation Entertainment Inc. stock rises Wednesday, outperforms market", "positive"),
Example("International Flavors & Fragrances Inc. stock rises Wednesday, still underperforms market", "negative"),
]

load_dotenv()
COHERE = os.getenv('COHERE')
FREE_NEWS_API = os.getenv('FREE_NEWS_API')

co = cohere.Client(COHERE)

def load_articles():
    conn = http.client.HTTPSConnection("free-news.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Host': "free-news.p.rapidapi.com",
        'X-RapidAPI-Key': FREE_NEWS_API
        }

    conn.request("GET", "/v1/search?q=stock%20market&lang=en&page=1", headers=headers)

    res = conn.getresponse()
    data = res.read()

    articles = json.loads(data)["articles"]
    return articles
def classify_articles(articles):
    
    titles = []
    dates = []
    i = 0
    for article in articles:
        titles.append(article["title"])
        date = datetime.strptime(article["published_date"], '%Y-%m-%d %H:%M:%S').timestamp()
        dates.append(int(date))
        i = i + 1
        if (i > 31):
            break

    classifications = co.classify(
        model='medium',
        taskDescription='Classify these as positive, negative',
        outputIndicator='Classify this stock',
        inputs=titles,
        examples =colin
    )

    output = []
    i = 0 
    for cl in classifications.classifications:
        output.append({
            'title': cl.input,
            'sentiment': cl.prediction,
            'date': dates[i],
            'confidence': {
                'positive': cl.confidence[0].confidence,
                'negative': cl.confidence[1].confidence
            }
        })
        i = i + 1

    return output

    # sum = 0.0

    # print("[")

    # for article in articles:
    #     if (article["summary"] == None):
    #         blob = TextBlob(article["title"])
    #         article["summary"] = "No Article"
    #     else:
    #         blob = TextBlob(article["summary"])
    #     senti = blob.sentiment.polarity
    #     sum += senti
    #     print("Example(\"" + article["title"] + "\", \"\"),")

    # print("]")
    
    # #print("OVERALL SENTIMENT: " + str(sum/len(articles)*5))

def run():
    articles = load_articles()
    classifications = classify_articles(articles)
    return classifications