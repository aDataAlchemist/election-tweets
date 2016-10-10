# -*- coding: UTF-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import config
import sys

#Much of this code comes from http://adilmoujahid.com/posts/2014/07/twitter-analytics/


class StdOutListener(StreamListener):
    def on_data(self, data_str):
        data = json.loads(data_str)
        if len(data['entities']['urls']) != 0:
            newdata = {'created_at' : data['created_at'], 'text' : data['text'],
                'hashtags' : [ hashtag['text'] for hashtag in data['entities']['hashtags'] ],
                'urls' : [ url['expanded_url'] for url in data['entities']['urls'] if url['url'] != '' ] }
            if len(newdata['urls']) != 0:
                print json.dumps(newdata)
        return True
    def on_error(self, status):
        print status

l = StdOutListener()
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
stream = Stream(auth, l)

print "Tracking tweets with the following terms: " + str(sys.argv[1:])
stream.filter(track=sys.argv[1:])
