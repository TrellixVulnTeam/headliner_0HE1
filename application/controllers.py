from application import app
from aylienapiclient import textapi
from .models import *
import requests
import json
import http.client, urllib.request, urllib.parse, urllib.error, base64




def get_articles(headline):

    # load json
    bing = app.config['BING_SEARCH']

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': bing,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'q': headline,
        'count': '10',
        'offset': '0',
        'mkt': 'en-us',
        'safeSearch': 'Moderate',
    })

    try:
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/news/search?%s" % params, "{body}", headers)
        print(conn)
        print(4)
        print(5)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # query the json, create article objects
    decoded_data = json.loads(data.decode())

    article_list = []

    for i in decoded_data['value']:
        # title, url, source, publication_date
        title = i['name']
        url = i['url']
        source = i['provider'][0]['name']
        date = i['datePublished']

        extra_data = article_extra_data(url)

        summary = extra_data[0]
        hashtags = extra_data[1]
        polarity = extra_data[2]
        polarity_confidence = extra_data[3]
        subjectivity = extra_data[4]
        subjectivity_confidence = extra_data[5]

        article_list.append(Article(title, url, source, date, summary, hashtags, polarity, polarity_confidence, subjectivity, subjectivity_confidence))

    return(article_list)

def article_extra_data(url):
    client = textapi.Client(app.config['AYLIEN_APP_ID'], app.config['AYLIEN_KEY'])
    extra_data = []

    summary_data = client.Summarize({'url': url, 'sentences_number': 3})
    summary = ""
    for sentence in summary_data['sentences']:
        summary += sentence
    extra_data.append(summary)

    hashtags = client.Hashtags({"url": url}) # is a list
    extra_data.append(hashtags)

    sentiment = client.Sentiment({'url': url})
    polarity = sentiment['polarity']
    extra_data.append(polarity)

    polarity_confidence = sentiment['polarity_confidence']
    extra_data.append(polarity_confidence)

    subjectivity = sentiment['subjectivity']
    extra_data.append(subjectivity)

    subjectivity_confidence = sentiment['subjectivity_confidence']
    extra_data.append(subjectivity_confidence)
    return extra_data





