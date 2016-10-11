import json
import sys
from collections import Counter

f = open(sys.argv[1], 'r')
topk = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 10
hashtags = []
for line in f:
    if line.startswith('{'):
        hashtags.extend(json.loads(line)['hashtags'])
hashtagCounter = Counter([hashtag.lower() for hashtag in hashtags])
for (hashtag, count) in hashtagCounter.most_common(topk):
    print hashtag, count
