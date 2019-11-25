#Building dataset
from sentiment_analysis.twitter_cred import twitter_api

#Fetch tweets with desired keyword for test dataset
def buildTestSet(keyword):
    try:
        #Use twitter api to fetch max 100 tweets
        tweets = twitter_api.GetSearch(keyword, count = 100)
        #How many tweets found
        print("Fetched " + str(len(tweets)) + " tweets for the term " + keyword)
        #return a list of tweets in the following format.
        return [{"text":status.text, "label":None} for status in tweets]
    except:
        #error if there is problem
        print("Something went wrong, check credentials")
        return None

#