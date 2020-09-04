# Overview
For news article data extraction, I have used Python to access news data. I have imported the newsapi package. Next, I set up news API to be used to pull news data.
Finally, I used the get_everything() method to extract news data. For the keywords mentioned in the assignment, I have extracted title, description, URL, content, 
source and author information. The complete code is also attached in a separate python script file named news_extraction.py.

## News API source
https://newsapi.org/

## Target Keywords

“Canada”, “University”, “Moncton”, “Halifax”, “Toronto”, “Vancouver”, “Alberta”, “Niagara”.

## File description

* news_extraction.py: This python script file has the code for API setup, news data extraction and data cleaning process.

* news_data_cleaned.json: This is the output JSON file with data extracted according to the target keywords.

## Data Cleaning

For the news related data, I have removed emoticons, symbols, pictographs, transport/map symbols, flags(iOS), special characters and tags. For removing the special tags,
I have used regex substitution. For cleaning all the emojis, symbols, etc. I have created a separate custom function named “clean_emoji”. This function also performs a 
regex operation to substitute and clean data.
