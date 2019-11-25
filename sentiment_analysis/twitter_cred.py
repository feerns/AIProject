import twitter

#initialize api instance
twitter_api = twitter.Api(consumer_key='YOUR_CONSUMER_KEY',
                          consumer_secret = 'YOUR_SECRET',
                          access_token_key = 'YOUR_TOKEN_KEY',
                          access_token_secret = 'YOUR_TOKEN_SECRET')
#test auth
print(twitter_api.VerifyCredentials())