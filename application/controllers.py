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
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # query the json, create article objects   
    decoded_data = json.loads(data.decode())

    article_list = []

    for i in decoded_data['value']:
        article = []
        # title, url, source, publication_date
        title = i['name']
        article.append(title)
        url = i['url']
        article.append(url)
        source = i['provider'][0]['name']
        article.append(source)
        date = i['datePublished']
        article.append(date)
        summary_data = client.Summarize({'url': url, 'sentences_number': 3}) # list
        article.append(summary_data['sentences'])
        hashtags = client.Hashtags({"url": url}) # is a list
        article.append(hashtags['hashtags'])
        sentiment = client.Sentiment({'url': url})
        polarity = sentiment['polarity']
        article.append(polarity)
        polarity_confidence = sentiment['polarity_confidence']
        article.append(polarity_confidence)
        subjectivity = sentiment['subjectivity']
        article.append(subjectivity)
        subjectivity_confidence = sentiment['subjectivity_confidence']
        article.append(subjectivity_confidence)

        article_list.append(article)

        # article_list.append(Article(title, url, source, date))

    return article_list


    # final_list = []
    # for article in article_list:
    #     final_list.append(article.title)
    #     final_list.append(article.url)
    #     final_list.append(article.source)
    #     final_list.append(article.publication_date)




# def article_extra_data(article_list):
#     client = textapi.Client(app.config['AYLIEN_APP_ID'], app.config['AYLIEN_KEY'])
#     extra_data = []

#     for article in article_list:
#         url = article.url

#         summary_data = client.Summarize({'url': url, 'sentences_number': 3})
#         summary = ""
#         for sentence in summary_data['sentences']:
#             summary += sentence
#         hashtags = client.Hashtags({"url": url}) # is a list
#         sentiment = client.Sentiment({'url': url})
#         polarity = sentiment['polarity']
#         polarity_confidence = sentiment['polarity_confidence']
#         subjectivity = sentiment['subjectivity']
#         subjectivity_confidence = sentiment['subjectivity_confidence']

#         extra_data.append(ExtraArticleData(summary, hashtags, polarity, polarity_confidence, subjectivity, subjectivity_confidence)) 


#     return extra_data



