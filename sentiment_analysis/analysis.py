from sentiment_analysis import dataset

keyword = input("Enter a keyword to search tweets with")
fetched_tweet = dataset.buildTestSet(keyword)