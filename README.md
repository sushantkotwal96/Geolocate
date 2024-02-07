# Geolocate Project Readme

## Project Overview

**Project Name:** Geolocate

**Description:** Geolocate is a Data Engineering project focused on extracting and analyzing tweets related to European football clubs in the English Premier League. The goal is to identify sentiments expressed by fans in tweets and visualize the global distribution of fanbases through an interactive dashboard.

You can view the project here: [Geolocate](https://lookerstudio.google.com/u/0/reporting/a4d60edc-eb51-4ce2-8616-b42c9faac1f3/page/p_jy33w1ri5c)

## Motivation

Football, being one of the most popular sports globally, has a significant impact on social media platforms. Geolocate aims to leverage the Twitter API (Tweepy) to extract and analyze tweets, providing insights into the geographic distribution of football fanbases. This information can be valuable for sporting organizations to understand the reach of the sport and plan targeted marketing campaigns.

## Key Features

- **Twitter API Integration:** Utilized Tweepy to extract tweet information, including geographical metadata.

- **Sentiment Analysis:** Conducted sentiment analysis on 250k+ tweets related to European football clubs using both TextBlob and Vader classifiers.

- **Data Preprocessing Workflow:** Orchestrated data preprocessing workflows using Apache Airflow to extract and structure tweet data efficiently.

- **Interactive Dashboard:** Developed an interactive dashboard using Google Looker Studio to visualize tweet sentiments and identify potential club fanbases across the world.

## Project Workflow

![Screenshot](image.png)

1) **Data Extraction using Tweepy:**
    * Leveraged the Tweepy client to extract Twitter data for every football club in the Premier League
    * Utilized academic access for obtaining tweet objects from Twitter, determining the response object and parameters
    * Maintained a list of football clubs based on the English Premier League
    * Extracted around 100 tweet objects for each club for the previous day, storing them in separate JSON files

2) **Data Transformation and Splitting:**
    * Separated tweet objects into two files: one containing tweet-related data and the other containing geographical data
    * Converted JSON files to CSV for each club, merging them into two final CSV files for tweet-related and geographical data

3) **Data Cleaning:**
    * Handled null values, replacing them with placeholders and removing tweets without location information
    * Calculated centroids of bounding boxes as tweet locations for mapping purposes


4) **Sentiment Analysis:** 
    * Removed stopwords, emoticons, and hashtags, tokenized and lemmatized the tweet text
    * Utilized TextBlob for sentiment analysis, considering polarity and subjectivity scores for positive, neutral, and negative sentiments
    * Employed the Vader classifier, optimized for handling tweets and informal language, providing intensity information ranging from -4 to 4
    * Stored sentiment data for visualization on the Looker Studio dashboard

5) **Dashboard Usage:**
    * Provided two dropdown lists on the dashboard for filtering by club and sentiment, allowing users to customize visualizations based on their preferences

## Dashboard

-   **The Dashboard below shows all the tweets for all the clubs and the locations across the world from where they are made**

    ![Screenshot](<Screenshot 2024-02-06 at 6.46.21 PM-1.png>)



-   **The user can select any club from the dropdown list to view the locations of the tweets for that respective club as shown here**

    ![Screenshot](<Screenshot 2024-02-06 at 6.52.56 PM.png>)



-   **The locations of tweets made for Bournemouth club are visualized here. This contains tweets for all sentiments since we the filter for sentiments is not yet placed**
    
    ![Screenshot](<Screenshot 2024-02-06 at 6.58.33 PM-1.png>)



-   **The user can then select any of the three sentiments from the dropdown list to view only the locations of that respective sentiment as shown here**

    ![Screenshot](<Screenshot 2024-02-06 at 6.56.43 PM.png>)



-   **The tweets with negative sentiments for the Bournemouth club are visualized here**

    ![Screenshot](<Screenshot 2024-02-06 at 7.00.12 PM-1.png>)



## Limitations

- **Limited Tweet Locations:** Due to limitations in obtaining actual coordinates, the project relies on bounding box centroids for tweet locations.

## Getting Started

To get started with the Geolocate project, follow these steps:

1. Clone the repository: `git clone [repository_url]`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Twitter API credentials.
4. Execute the data extraction and analysis scripts.

## Acknowledgments

The Geolocate project acknowledges the use of the Twitter API, Tweepy, TextBlob, Vader, Apache Airflow, and Google Looker Studio for enabling data extraction, sentiment analysis, workflow orchestration, and dashboard visualization.


## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.

Feel free to contribute, report issues, or suggest improvements to make Geolocate even better!
