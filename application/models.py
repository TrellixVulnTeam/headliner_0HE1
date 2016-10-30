class Article():
	def __init__(self, title, url, source, publication_date, summary, hashtags, polarity, polarity_confidence, subjectivity, subjectivity_confidence):
		self.title = title
		self.url = url
		self.source = source
		self.publication_date = publication_date
		self.summary = summary
		self.hashtags = hashtags
		self.polarity = polarity
		self.polarity_confidence = polarity_confidence
		self.subjectivity = subjectivity
		self.subjectivity_confidence = subjectivity_confidence

