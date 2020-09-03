import pymongo
import newsapi as ns
import re

# user credentials to access the news API
my_key = ('dc26749994374766a2394e60ac6bd447')

# set up news api to be used to pull data
newsapi = ns.NewsApiClient(api_key=my_key)

# setup db and collection for MongoDB
my_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
my_db = my_client["Asgmt3"]
my_collection = my_db["news"]

news = []   # empty list to which new_details obj will be added
print ("Initializing search...")

# search keywords
search_keywords = ['Canada', 'University', 'Dalhousie University', 'Halifax', 'Canada  Education', 'Moncton', 'Toronto']

# API call from https://newsapi.org/
for keyword in search_keywords:
    f = open("output.txt","a+")
    for article in newsapi.get_everything(q=keyword, page_size=100)['articles']:
        news_details = {'description': article['description'], 'title': article['title'],
                        'url': article['url'], 'content': article['content'],
                        'source': article['source'], 'author': article['author']
                        }

        # special tags regex reference: https://www.webdeveloper.com/d/199621-need-a-regex-to-exclude-all-but-a-za-z0-9s
        if news_details['description'] is not None:
            news_details['description'] = re.sub(r'[^a-zA-Z0-9\s\.]+', '', news_details['description'])
            f.write(news_details['description'])  # write data to "output.txt", will be used later for frequency count
        if news_details['title'] is not None:
            news_details['title'] = re.sub(r'[^a-zA-Z0-9\s\.]+', '', news_details['title'])
        if news_details['content'] is not None:
            news_details['content'] = re.sub(r'[^a-zA-Z0-9\s\.]+', '', news_details['content'])
        if news_details['author'] is not None:
            news_details['author'] = re.sub(r'[^a-zA-Z0-9\s\.]+', '', news_details['author'])
        news.append(news_details)
    f.close()
print ("Data cleaning finished")

# sending data to mongoDB
my_collection.insert_many(news)
print('Data stored successfully in MongoDB')