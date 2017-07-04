#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json

consumer_key = 'SUlH8nWOi57LxnzfLXP1cvRJi'
consumer_secret = 'cUeNzMUwAjQ7ee5Rpkh6MuKSIQgofaZjvmqieJMDQqDUJvsRpG'
access_token = '881863248353652736-mtltzS5wgQle0VocDgGrOyBJrDLnFig'
access_token_secret = 'D9DZpbfnAgWL9ouYmZc1ljzCnV21I2xz9lGp15QrQC1Zv'



def get_all_tweets(screen_name):
    print screen_name
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []
        
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name, count=200000)
        
    #save most recent tweets
    alltweets.extend(new_tweets)
        
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
        
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
                
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
                
        #save most recent tweets
        alltweets.extend(new_tweets)
                
        #update the id of the oldest tweet less one
        oldest = alltweets[len(alltweets)-1].id - 1
                
        print "...%s tweets downloaded so far" % (len(alltweets))
        
    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [{'id_str' : tweet.id_str, 'created_at' : str(tweet.created_at), 'tweet':tweet.text.encode("utf-8")} for tweet in alltweets]
        
    #write the csv
    jsonfile = open('/Users/KangHaoPeng/Documents/g0v/HouseTweets/' + screen_name + 's_tweets.json', 'w')
    json.dump(outtweets, jsonfile)
    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download

    f = open('/Users/KangHaoPeng/Documents/g0v/house-members-propublica.json', 'r')
    r = f.read()

    length = len(r)
    i = 0
    j = 0
    start = False
    while(i+14 < length):
        if (r[i:i+15]=='twitter_account'):
            i = i + 19
            j = i
            while(r[j:j+1] != '"') :
                j = j+1
        
            if(i >= j):
                continue
        
            if(start):
                get_all_tweets(r[i:j])
            
            if(r[i:j] == 'TiberiPress'):
                start = True
        i = i+1

