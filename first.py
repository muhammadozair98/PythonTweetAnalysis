tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"
tweet_words = tweet_string.split()
number_of_words = len(tweet_words)
print("Number of words in this tweet is: " + str(number_of_words))

print("words in the tweet are")

for w in tweet_words:
    print("The number of letters in " + w + " is " + str(len(w)))

print("End of the words in the tweet")
