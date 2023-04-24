# Coronavirus Twitter Analysis

In this project, I analyzed a dataset containing geotagged tweets sent in 2020. The primary goal of this analysis was to determine the amount of times a hashtag related to COVID-19 was used in a tweet; this information can be utilized to identify trends among users on Twitter. However, please note that only about 2% of tweets are geotagged, which means that this analysis may not be representative of Twitter’s overall user base. 

## Procedure

**MapReduce:**

During my analysis, I utilized a procedure called [MapReduce](https://en.wikipedia.org/wiki/MapReduce), which is often used for large scale parallel processing. MapReduce involves three steps: partition, map, and reduce. Since the given dataset contained tweets that were already split into one file per day, the partition step was already completed. My task was to implement the map and reduce steps.

**Map:**

The `map.py` file takes in a zip file for an individual day and counts the number of times that a certain hashtag was used during that day based on one of two parameters—either language or country. In order to loop over each file (i.e. day) in the dataset, I created a shell script called `run_maps.sh`.

**Reduce:**

The output of the `map.py` file is stored in the `outputs` folder, which contains a file for each day of the year. Once it has run on all files, the `reduce.py` file is used to combine all of the files in the `outputs` folder into a single file, which is either called `reduced.lang` or `reduced.country` (depending on whether language or country was the input parameter). This file contains the total number of times each hashtag was used in 2020.

**Visualize:**

Once the data has been consolidated into a single file, I was able to perform data visualizations using the `matplotlib` library. The `visualize.py` file takes in a hashtag and either `reduced.lang` or `reduced.country` as its input parameters and creates a bar graph that visually displays the top 10 languages or countries in which the hashtag was used the most. Here are some examples:

The following command:
```
$ ./src/visualize.py --input_path=reduced.lang --key='#coronavirus'
```
outputs:

### Number of Tweets Containing #coronavirus (Top 10 Languages)
<img src=https://github.com/Kevinl0378/twitter_coronavirus/blob/master/%23coronavirus_bar_graph_(language).png />

The following command:
```
$ ./src/visualize.py --input_path=reduced.country --key='#coronavirus'
```
outputs:

### Number of Tweets Containing #coronavirus (Top 10 Countries)
<img src=https://github.com/Kevinl0378/twitter_coronavirus/blob/master/%23coronavirus_bar_graph_(country).png />

The MapReduce procedure even works with hashtags in languages other than English. For example:

The following command:
```
$ ./src/visualize.py --input_path=reduced.lang --key='#코로나바이러스'
```
outputs:

### Number of Tweets Containing #코로나바이러스 (Top 9* Languages)
<img src=https://github.com/Kevinl0378/twitter_coronavirus/blob/master/%23코로나바이러스_bar_graph_(language).png />

The following command:
```
$ ./src/visualize.py --input_path=reduced.country --key='#코로나바이러스'
```
outputs:

### Number of Tweets Containing #코로나바이러스 (Top 10 Countries)
<img src=https://github.com/Kevinl0378/twitter_coronavirus/blob/master/%23코로나바이러스_bar_graph_(country).png />

## Alternative Reduce:

I also created a file called `alternative_reduce.py`, which takes in a list of hashtags and creates a line on a line graph for each hashtag. This file can be thought of as a combined version of the `reduce.py` and `visualize.py` files, as it looks through the data in the `outputs` folder, determines the number of times a particular hashtag was used on each day, and performs visualizations on its findings. The line graph can be utilized to track the usage of a particular hashtag (or a group of hashtags) throughout 2020. Here are some interesting examples:

The following command:
```
$ ./src/alternative_reduce.py --input_hashtags '#coronavirus' '#covid19' '#flu' '#doctor'
```
outputs:

### Number of Tweets Containing Either #coronavirus, #covid19, #flu, or #doctor Throughout 2020
<img src=https://github.com/Kevinl0378/twitter_coronavirus/blob/master/%23coronavirus_%23covid19_%23flu_%23doctor_line_graph.png />

The following command:
``` 
$ ./src/alternative_reduce.py --input_hashtags '#cough' '#sneeze'
```
outputs:

### Usage of #cough vs. #sneeze Throughout 2020
<img src=https://github.com/Kevinl0378/twitter_coronavirus/blob/master/%23cough_vs_%23sneeze_line_graph.png />

The following command:
```
$ ./src/alternative_reduce.py --input_hashtags '#coronavirus' '#covid19' '#covid-19' '#covid2019' '#covid-2019'
```
outputs:

### Number of Tweets Containing Different Versions of #coronavirus Throughout 2020
<img src=https://github.com/Kevinl0378/twitter_coronavirus/blob/master/different_versions_of_%23covid19_line_graph.png />
