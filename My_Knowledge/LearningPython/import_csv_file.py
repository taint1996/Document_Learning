from pymongo import MongoClient
from bs4 import BeautifulSoup
import csv

client = MongoClient()
db = client.raw_database
print(db.twitter_post)

DELIMITER_CHAR = '\t'

# with open('twitter_tweets.csv', 'rt', encoding='utf8') as csvfile:
with open('/home/local/ELARION/taint/Robin8_Project/haowei_pipeline/test/twitter_data_test.csv', 'rt', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    result = []
    for row in csvreader:
      if row:
        values = row[0].split(DELIMITER_CHAR)

        result.append({
            'id': int(values[0]),
            'crawler_time': values[1],
            'crawler_time_stamp': int(values[2]) // 1000,
            'screen_name': values[3],
            'user_at_name': values[4],
            'user_id': values[5],
            'is_v': values[6],
            'tx_url': values[7],
            'pub_time': values[8],
            'pub_time_stamp': int(values[9]),
            'url': values[10],
            'tweet_id': values[11],
            'tweet_content': values[12],
            'reply_cnt': int(values[13]),
            'retweets_cnt': int(values[14]),
            'like_cnt': int(values[15]),
            'is_retweet': int(values[16]),
            'r_user_screen_name': values[17],
            'r_user_at_name': values[18],
            'r_use_id': values[19],
            'r_url': values[20],
            'r_tweet_id': values[21],
            'r_tweet_content': values[22],
        })
print(result)
post = db.twitter_post
post.insert(result)
print(post.count())




