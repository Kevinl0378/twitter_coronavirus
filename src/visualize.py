#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

keys = []
values = []
for k,v in items[:10]:
    print(k,':',v)
    keys = [k] + keys
    values = [v] + values
    print(keys, values)

index = range(len(keys))
plt.rcParams["figure.figsize"] = (10,8)
plt.bar(index, values, color = 'lightcoral', width=0.30)
plt.xticks(index, [x.upper() for x in keys])
plt.ylabel("Number of Tweets", labelpad=10)
#plt.show()
if 'lang' in args.input_path:
    plt.xlabel("Language")
    plt.savefig(f'{args.key}_bar_graph_(language).png')
else:
    plt.xlabel("Country")
    plt.savefig(f'{args.key}_bar_graph_(country).png')
