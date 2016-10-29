from application import app
import requests
import json
import http.client, urllib.request, urllib.parse, urllib.error, base64




def get_articles(headline):
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
    return(data)




