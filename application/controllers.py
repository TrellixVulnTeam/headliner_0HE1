from application import app
from aylienapiclient import textapi
from .models import *
import requests
import json
import http.client, urllib.request, urllib.parse, urllib.error, base64




def get_articles(headline):
    client = textapi.Client(app.config['AYLIEN_APP_ID'], app.config['AYLIEN_KEY'])

    # load json
    bing = app.config['BING_SEARCH']

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': bing,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'q': headline,
        'count': '15',
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
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # query the json, create article objects   
    decoded_data = json.loads(data.decode())

    article_list = []

    for i in decoded_data['value']:

        title = i['name']   
        url = i['url']
        source = i['provider'][0]['name']
        date = i['datePublished']
        summary_data = client.Summarize({'url': url, 'sentences_number': 3}) # list
        summary = summary_data['sentences']
        hashtags_data = client.Hashtags({"url": url}) # is a list
        hashtags = hashtags_data['hashtags']
        sentiment = client.Sentiment({'url': url})
        polarity = sentiment['polarity']
        polarity_confidence = sentiment['polarity_confidence']
        subjectivity = sentiment['subjectivity']
        subjectivity_confidence = sentiment['subjectivity_confidence']
        article_list.append(Article(title, url, source, date, summary, hashtags, polarity, polarity_confidence, subjectivity, subjectivity_confidence))
 
    return article_list





