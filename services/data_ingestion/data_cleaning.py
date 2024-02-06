import pandas as pd
import os
from twitter_etl import get_clubs

def merge_csv(RESOURCE_PATH, data, league, club_file):

    if data == 'club':
        file_path = RESOURCE_PATH + 'csv/' + league + club_file
    elif data =='place':
        file_path = RESOURCE_PATH + 'csv/' + league + 'places/'

    file_list = os.listdir(file_path)
    file_list.sort()
    data_merged = pd.DataFrame()

    for file in file_list:
        data_df = pd.read_csv(file_path + file, dtype='unicode')
        if data == 'club':
            data_df = refine_club_data(data_df)
        data_df['Club_Name'] = file.split('.')[0]
        data_merged = pd.concat([data_merged, data_df], ignore_index=True)

    data_merged.to_csv(RESOURCE_PATH + 'csv/' + league + 'merged_data/' + data + '_merged.csv', encoding='utf-8', index = False)

    return data_merged
        

def refine_club_data(club_df):
    refined_club_df = club_df[['created_at','id','full_text','retweet_count', 'favorite_count', 'user.id', 'user.name', 'user.location', 'user.followers_count', 'user.friends_count', 'user.favourites_count']]
    return refined_club_df


def main():
    league = 'premierleague'
    club_file = 'plclubs'
    RESOURCE_PATH = '../../resources/'
    club_data_merged = merge_csv(RESOURCE_PATH, 'club', league + '/', club_file + '/')
    place_data_merged = merge_csv(RESOURCE_PATH, 'place', league + '/', club_file + '/')


if __name__ == "__main__":
    main()