"""
anything here will be commented!

To evaluate the good or bad score of a twee, we cout the number of good and bad words in it

if a word is good , increse the value of good_words by one
if a word is bad , increse the value of bad_words by one

if good_words > bad_words then its a good_tweet otherwise is a bad one

"""
#tweet_words = tweet_string.split()

#making for loop
#number_of_good_words = 0
#number_of_bad_words = 0
#good_words = ["Thanks","historic","paychecks"]
#bad_words = ["taxes"]

import json
import nltk #importing the package, not our code. tell python we want to use this over here
import twitter
from nltk.stem.porter import*

#This authenticates my twitter app
twitter_api = twitter.Api(consumer_key='Fv4gGwP3brFhiMEnlZO9WHX7I',
                      consumer_secret='MAtCQj6ObPcsynM8DThhuVqSREQ9UXGFLWvOpfhCac0IZB0mIB',
                      access_token_key='980931878697029632-szLBZqVy7CUzriU1EzXBznI8x4FucGZ',
                      access_token_secret='rPNZY5oNTcbgjGc6nRRcDCMlpLMMN10OgtwrF33sK38WB',
                      tweet_mode='extended' )

stemmer = PorterStemmer()

#Breakdown sentance to words
def get_words(str):  #function1
    return nltk.word_tokenize(str)  #word_tokenize is a function thats not ours


def get_average_word_weight(list_of_words, word_weights): #Function2
    number_of_words = len(list_of_words);
    sum_of_word_weight = 0.0
    for w in list_of_words:
        stemmed_word = stemmer.stem(w)
        if stemmer.stem(w) in word_weights:
            sum_of_word_weight += word_weights[stemmed_word] #in checks the membership o w in good_words list
        #else:
        #    print (' " ' + stemmed_word + ' ":0.0,')
    return sum_of_word_weight/number_of_words

# tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"
# need to call this function and give it a string to analyze define only
def anaylse_tweet (tweet_string, word_weights):
    words = get_words(tweet_string)
    ave_tweet_weight = get_average_word_weight (words, word_weights)
    print ("The weight  of the tweet is " + str(ave_tweet_weight))

    if ave_tweet_weight > 0:
        print("Its a good tweet")
    else:
        print("Its a bad tweet")

#read tweets from outside source  #and close file
def read_from_files(json_file, tweet_file):
    #json_file = "word_weights.json"
    #tweet_file= "tweets.txt"
        #empty dictionary defined
    word_weights = {}
    with open (json_file) as f:  #open json file and call it f
        s = f.read() #storing file into s... reading the whole file
        word_weights = json.loads(s) #load the string NOW it is a dictionary
#list of tweets
    tweets = twitter_api.GetUserTimeline(screen_name="realDonaldTrump", count=10)
    for tweet in tweets:  #give file handler to a for loop. Python opens up and asisigns first line to the value.
        print (tweet.full_text) #I only need tweet.full_text ........ acsess json file with a "." infont of the name
        anaylse_tweet(tweet.full_text, word_weights)
        print ("---------------------------------------------------------")
        #Come back in loop and assign tweet to the second line.
read_from_files("word_weights.json", "tweets.txt")
