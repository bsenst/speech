import json
import snscrape.modules.twitter as sntwitter

# https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af
# Creating list to append tweet data to
tweets = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:knowmedge').get_items()):
    if i>25:
        break
    tweets.append([tweet.url, str(tweet.date.utcnow()), tweet.content])

with open('tweets.json', 'w', encoding='utf-8') as outfile:
    json.dump(tweets, outfile)
