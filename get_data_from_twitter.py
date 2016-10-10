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
        if 'entities' in data and 'urls' in data['entities'] and len(data['entities']['urls']) != 0:
            newdata = {}
            if 'created_at' in data:
                newdata['created_at'] = data['created_at']
            if 'text' in data:
                newdata['text'] = data['text']
            if 'hashtags' in data['entities']:
                newdata['hashtags'] = [ hashtag['text'] for hashtag in data['entities']['hashtags'] ],
            newdata['urls'] = [ url['expanded_url'] for url in data['entities']['urls'] if 'url' in url and 'expanded_url' in url and url['url'] != '' ]
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
