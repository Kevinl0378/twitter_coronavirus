#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_hashtags', nargs='+', required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict 
import matplotlib.pyplot as plt

master_total = {}

for hashtag in args.input_hashtags:

    total_lang = {}
    total_country = {}
    
    # Totaling the number of usages for each hashtag
    for file in sorted(os.listdir('outputs')):
        file_in_outputs = os.path.join('outputs', file)
        date = file_in_outputs[18:26]
        
        if os.path.isfile(file_in_outputs):
            if 'lang' in file_in_outputs:
                #print("file_in_outputs=", file_in_outputs)
                total_tweets_lang = 0
                with open(file_in_outputs) as f:
                    tmp = json.load(f)
                    for k in tmp:
                        if k == hashtag: ##### hashtag here
                            for key in tmp[k]:
                                total_tweets_lang += tmp[k][key]
                total_lang[date] = total_tweets_lang
                #print("total_tweets_lang=", total_tweets_lang)
            else:
                total_tweets_country = 0
                with open(file_in_outputs) as f:
                    tmp = json.load(f)
                    for k in tmp:
                        if k == hashtag: ##### hashtag here
                            for key in tmp[k]:
                                total_tweets_country += tmp[k][key]
                total_country[date] = total_tweets_country
   

    # CHECK IF TOTALS MATCH
    days_matching = 0
    for k,v in total_lang.items():
        if total_country[k] == v:
            days_matching += 1
        else:
            raise Exception('Total tweets were not equal')
    if days_matching == 366:
        print("days_matching=", days_matching, "--> passed!")
        master_total[hashtag] = total_lang

print(master_total)
# CREATE LINE PLOT
plt.figure(figsize=(12,9))
dates = []
for hashtag, total in master_total.items():
    keys = []
    values = []
    for k, v in total.items():
        keys.append(k)
        dates.append(k)
        values.append(v)
    plt.plot(range(len(keys)), values, label = hashtag)
plt.xlabel("Date", labelpad=8)
plt.ylabel("Number of Tweets Using the Hashtag", labelpad=25)
plt.xticks(range(len(keys))[::15], dates[::15], rotation = 60)
plt.legend()
#plt.savefig("#cough_vs_#sneeze_line_graph.png")
