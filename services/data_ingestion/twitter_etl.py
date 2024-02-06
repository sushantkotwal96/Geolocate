import tweepy
import pandas as pd
import json
import os
import sys
filepath = os.path.abspath(__file__ +'/../')
sys.path.append(filepath)
#from config import *

def get_twitter_client():
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    client = tweepy.Client(BEARER_TOKEN, 
                            CONSUMER_KEY, 
                            CONSUMER_SECRET, 
                            ACCESS_KEY, 
                            ACCESS_SECRET, 
                            return_type = dict, 
                            wait_on_rate_limit=True)

    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    return client, api

def get_clubs(RESOURCE_PATH, league, club_file):

    # f'{RESOURCE_PATH}/text/{league}{club_file}{club_file[:-1]}.txt'
    with open(RESOURCE_PATH + 'text/' + league + club_file + club_file[:-1] + '.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
        clubs_str = ''.join(text)

    clubs = []
    for club in clubs_str.split(", "):
        clubs.append(club)
    return clubs

def get_tweets(n_tweets, client, api, league, club_file, RESOURCE_PATH):
    
    clubs = get_clubs(RESOURCE_PATH, league, club_file)
    for club in clubs:

        print(f'Calling tweepy API referencing {league} clubs')
        tweets = api.search_tweets(
                                    q =  club + ' -filter:retweets',
                                    include_ext_edit_control = True,
                                    tweet_mode = 'extended',
                                    count = n_tweets,
                                    lang = 'en',
                                    include_entities = False
        )
        print(f'Successfully extracted tweets from the API for {league} clubs')
        club = club.replace(" ","")
        print(f'Storing tweets and updating JSON for {league} clubs')

        store_tweets(RESOURCE_PATH, league, club_file, tweets['statuses'], club)

        print(f'Tweets JSON data updated')
        print(f'Storing places and updating JSON for {league} clubs')

        store_places(RESOURCE_PATH, league, tweets['statuses'], club)
        
        print(f'Places JSON data updated')


def store_tweets(RESOURCE_PATH, league, club_file, tweets, club):

    tweets_path = RESOURCE_PATH + 'json/' + league + club_file + club + '.json'
    for tweet in tweets:
        tweet_data = {}
        try:
            with open(tweets_path, 'r', encoding = 'utf-8') as f:
                tweet_data = json.loads(f.read())
            tweet_data['statuses'].append(tweet)
        except:
            print(f'No data found for {club} club. Creating new data ...')
            tweet_data = {"statuses": []}
            tweet_data['statuses'].append(tweet)
        finally:
            with open(tweets_path, 'w', encoding = 'utf-8') as f:
                json.dump(tweet_data, f, ensure_ascii=False, indent=4)
            

def store_places(RESOURCE_PATH, league, tweets, club):

    place_path = RESOURCE_PATH + 'json/' + league + 'places/' + club + '.json'
    for tweet in tweets:
        if tweet['place']:
            tweet['place']['tweet_id'] = tweet['id']
            place_data = {}
            try:
                with open(place_path, 'r', encoding='utf-8') as f:
                    place_data = json.loads(f.read())
                place_data['data'].append(tweet['place'])
            except:
                print(f'No data found for {club} club. Creating new data ...')
                place_data = {"data":[]}
                place_data['data'].append(tweet['place'])
            finally:
                with open(place_path, 'w', encoding='utf-8') as f:
                    json.dump(place_data, f, ensure_ascii=False, indent=4)


def json_to_csv(RESOURCE_PATH, data, league, club_file):
        
        if data == 'club':
            json_file_path = RESOURCE_PATH + 'json/' + league + club_file
            csv_file_path = RESOURCE_PATH + 'csv/' + league + club_file
        elif data == 'place':
            json_file_path = RESOURCE_PATH + 'json/' + league + 'places/'
            csv_file_path = RESOURCE_PATH + 'csv/' + league +'places/'

        df = pd.DataFrame()

        file_list = os.listdir(json_file_path)
        file_list.sort()

        print(f'Converting updated JSON data into CSV format for {data} files referencing {league} clubs')
        for file in file_list:
            try:
                with open(json_file_path + file, 'r', encoding='utf-8') as f:
                    json_data = json.loads(f.read())
            except:
                continue
            if data == 'club':
                df = pd.json_normalize(json_data['statuses'])
            elif data == 'place':
                df = pd.json_normalize(json_data['data'])
            
            club = file.split('.')[0]
            df.to_csv(csv_file_path + club + '.csv', encoding='utf-8', index = False)

        print(f'Successfully created CSV files for {data} files referencing {league} clubs')

def run_twitter_etl_pipeline(league, n_tweets):
    
    #client, api = get_twitter_client()
    RESOURCE_PATH = '../../resources/'
    club_file = 'plclubs'

    #get_tweets(n_tweets, client, api, league + '/', club_file + '/', RESOURCE_PATH)
    json_to_csv(RESOURCE_PATH, 'club', league + '/', club_file + '/')
    json_to_csv(RESOURCE_PATH, 'place', league + '/', club_file + '/')

if __name__ == "__main__":
    league = 'premierleague'
    n_tweets = 100
    run_twitter_etl_pipeline(league, n_tweets)


# CODE LOGIC
# EXTRACTING TWEETS AND PUSHING THEM INTO A JSON FILE. UPDATING/APPENDING JSON FILE ON EACH API CALL
# UPDATED JSON FILE IS THEN CONVERTED INTO CSV FILE
# THE CSV FILES ARE THEN MERGED AND REFINED TO SELECT IMPORTANT COLUMNS FOR FURTHER STEPS

# if __name__ == "__main__":
#     league = 'premierleague'
#     n_tweets = 100
#     run_twitter_etl_pipeline(league, n_tweets)

