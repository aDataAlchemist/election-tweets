# election-tweets

To get this to run, rename config_example.py to config.py and update the felds accordingly with your credentials.

Run the following script to get the twitter data:

```
python get_data_from_twitter.py [list of space separated keywords]
  e.g. python get_data_from_twitter.py "#Hillary2016" "#imwithher"
```
This will print the data to standard out, so it may make sense to pipe the output to a file

Run the following script to get the top hashtags from the previous data set:

```
python get_top_hashtags.py [input file] [optional number of hashtags to return]
```
