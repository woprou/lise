from managedata.mining.classification import AnalyzeVader
from managedata.mining.organization import Organization
from managedata.models import Keyword, Business, Review, Opinion, Weekday
import googlemaps as g

class CollectRival(object):

    def __init__(self, businessPlan):
        self.category = businessPlan.category
        self.keywords = Keyword.objects.filter(category=self.category)
        self.address = businessPlan.location()
        self.client = g.Client('AIzaSyB0UBbtTXcMS8DrdviSLxab9Oa0B_Dcclg')
        self.location = self.client.geocode(self.address)[0]['geometry']['location']


    def add_ids(self, result):
        places_ids = list(map(lambda x: x.place_id, Business.objects.filter(category=self.category)))
        for place in result:
            if place['place_id'] not in places_ids:
                business = Business.objects.create(name=place['name'],
                                        place_id=place['place_id'],
                                        category=self.category,
                                        location=place['geometry']['location'])
                self.collect_opening_hours(place['place_id'], business)



    def collect_opening_hours(self, place_id, business):
        result = g.places.place(self.client, place_id, language=None)['result']
        if 'opening_hours' in result:
            for item in result['opening_hours']['weekday_text']:
                items = item.split(': ')
                Weekday.objects.create(weekday=items[0], hours=items[1], business=business)


    def placesAll(self):
        placesList = []
        for query in self.keywords:
            result = self.client.places(query, self.location)
            locais = filter(self.isNear, result['results'])
            self.add_ids(locais)
            while 'next_page_token' in result:
                try:
                    next = result['next_page_token']
                    result = self.client.places(query, self.location, page_token=next)
                    locais = filter(self.isNear, result['results'])
                    self.add_ids(locais)
                except:
                    continue
        return placesList

    def isNear(self, local):
        coo = local['geometry']['location']
        return (abs(self.location['lat'] - coo['lat']) <= 0.3 and abs(self.location['lng'] - coo['lng']) <= 0.3)


class CollectReview(object):

    def __init__(self, businessPlan):
        self.category = businessPlan.category
        self.client = g.Client('AIzaSyB0UBbtTXcMS8DrdviSLxab9Oa0B_Dcclg')


    def reviewAll(self):
        places_ids = list(map(lambda x: x.place_id, Business.objects.filter(category=self.category)))
        reviews_ids = list(map(lambda x: x.review_id, Review.objects.filter(business__category=self.category)))
        for id in places_ids:
            result = g.places.place(self.client, id, language=None)['result']
            business = Business.objects.get(place_id=id)
            for review in result.setdefault('reviews', {}):
                review_id = review['author_url'].split('/')[5] + '/' + id if review.get('author_url') else False
                if review_id not in reviews_ids and review['text'] != '':
                    review = Review.objects.create(review_id=review_id, complete_text=review['text'], business=business)
                    self.saveOpinions(review)


    def saveOpinions(self, review):
        org = Organization()
        sentences = org.separate_sentences(review.complete_text)
        pattern = org.pattern_regex('managedata/util/stopwords.txt')
        sentences_dict = org.generate_keywords(sentences, pattern)
        vader = AnalyzeVader()
        for sentence in sentences_dict.items():
            polarity = vader.polarity(sentence[0])
            lemmatized = ' '.join(map(lambda x: x.lemma, org.tokens_cogroo(sentence[1])))
            Opinion.objects.create(text_pt=sentence[1], text_en=sentence[0], polarity=polarity, review=review, lemmatized=lemmatized)






