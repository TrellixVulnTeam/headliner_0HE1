from application import app
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

        article_list.append(Article(title, url, source, date))

    # change to return block of data
    return(big_list)








