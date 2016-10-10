import json
import sys
from collections import Counter

f = open(sys.argv[1], 'r')
hashtags = []
for line in f:
    if line.startswith('{'):
        hashtags.extend(json.loads(line)['hashtags'])
hashtagCounter = Counter([hashtag.lower() for hashtag in hashtags])
for (hashtag, count) in hashtagCounter.most_common(30):
    print hashtag, count
