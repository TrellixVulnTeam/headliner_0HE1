class Article():
	def __init__(self, title, url, source, publication_date):
		self.title = title
		self.url = url
		self.source = source
		self.publication_date = publication_date

	def extra_data(self):
		client = textapi.Client(app.config['AYLIEN_APP_ID'], app.config['AYLIEN_KEY'])
		extra_data = []

		url = self.url

		summary_data = client.Summarize({'url': url, 'sentences_number': 3})
		summary = ""
		for sentence in summary_data['sentences']:
			summary += sentence
		hashtags = client.Hashtags({"url": url}) # is a list
		sentiment = client.Sentiment({'url': url})
		polarity = sentiment['polarity']
		polarity_confidence = sentiment['polarity_confidence']
		subjectivity = sentiment['subjectivity']
		subjectivity_confidence = sentiment['subjectivity_confidence']

		extra_data.append(ExtraArticleData(summary, hashtags, polarity, polarity_confidence, subjectivity, subjectivity_confidence)) 

		return extra_data


		# Article.extra_data()[i].summary


class ExtraArticleData():
	def __init__(self, summary, hashtags, polarity, polarity_confidence, subjectivity, subjectivity_confidence):
		self.summary = summary
		self.hashtags = hashtags
		self.polarity = polarity
		self.polarity_confidence = polarity_confidence
		self.subjectivity = subjectivity
		self.subjectivity_confidence = subjectivity_confidence
		