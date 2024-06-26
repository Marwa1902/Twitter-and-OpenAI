import openai
import pandas as pd
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import textwrap

# openAI API key
openai.api_key = 'API KEY'

# set up geopy geolocator
geolocator = Nominatim(user_agent="tweet_location_comparison")

def extract_location_from_openai_response(response_text):
    lines = response_text.split('\n')
    for line in lines:
        if line.startswith("Mentioned Location:"):
            mentioned_location = line.replace("Mentioned Location:", "").strip()
            # if the mentioned location contains both city and state
            if '(' in mentioned_location and ')' in mentioned_location:
                return mentioned_location.split('(')[1].split(')')[0].strip()
            else:
                return mentioned_location
    return "Unknown"

def categorize_location_match(mentioned_location, geolocation_text):
    # if the mentioned location is in the geolocation_text
    if mentioned_location.lower() in geolocation_text.lower():
        # if it's a country, city, or exact location match
        if mentioned_location.lower() == geolocation_text.lower():
            return 'exact_location'
        elif mentioned_location.lower() in geolocation_text.lower().split(','):
            return 'city_match'
        elif mentioned_location.lower() in geolocation_text.lower():  # if mentioned location is a country
            return 'country_match'
    return 'unknown_match'


def generate_detailed_response(tweet_row):
    user_prompt = f"Extract user's location and the location mentioned in the tweet:" \
                  f"\n\n{tweet_row['text']}\n\nInformation to retrieve: user_location, mentioned_location," \
                  f" country, city, date, time, events, mentions, and any other relevant details."

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_prompt,
            max_tokens=800,
            temperature=0.7
        )
        detailed_response = response.choices[0].text.strip()

        # extract mentioned location from OpenAI response
        mentioned_location_text = extract_location_from_openai_response(detailed_response)

        # comparison of mentioned_location with geolocationS
        geolocation = (tweet_row['latitude'], tweet_row['longitude'])

        # convert latitude and longitude to a location
        location = geolocator.reverse(geolocation)
        geolocation_text = location.address if location else f"({geolocation[0]}, {geolocation[1]})"

        # print the original tweet and detailed response
        print("Original Tweet:")
        print(tweet_row['text'])
        print("\nDetailed Response:")
        print(detailed_response)

        # print the mentioned location and geolocation for comparison
        print(f"Mentioned Location (from text): {mentioned_location_text}")
        print(f"Geolocation (from latitude and longitude): {geolocation_text}")

        # compare mentioned_location_text with geolocation_text
        if mentioned_location_text == "Unknown":
            print("No location mentioned")
            print('-' * 50)
            return 'no_mention'

        match_category = categorize_location_match(mentioned_location_text, geolocation_text)

        if match_category == 'exact_location':
            print("Exact Location Match")
            print('-' * 50)
            return 'exact_location'
        elif match_category == 'city_match':
            print("City Match")
            print('-' * 50)
            return 'city_match'
        elif match_category == 'country_match':
            print("Country Match")
            print('-' * 50)
            return 'country_match'
        else:
            # if it's not a match, it's a mismatch
            print("Mismatch: Mentioned location does not match geolocation")
            print('-' * 50)
            return 'mismatch'

    except Exception as e:
        print(f"Error generating OpenAI response: {e}")
        return 'error'

# read the tweet data from the CSV file
tweet_data = pd.read_csv("cleaned_dataset.csv")

# select 1000 random tweets from the dataset
random_tweets = tweet_data.sample(n=1000, random_state=42)

# initialize counts for different match categories
exact_location_count = 0
city_match_count = 0
country_match_count = 0
mismatch_count = 0
no_location_mentioned_count = 0  

# iterate through each row and generate detailed responses for the selected random tweets
for index, row in random_tweets.iterrows():
    # check if latitude and longitude are present
    if pd.notna(row['latitude']) and pd.notna(row['longitude']):
        # generate detailed response and compare mentioned_location with geolocation
        result = generate_detailed_response(row)

        # update counts based on the result
        if result == 'no_mention':
            no_location_mentioned_count += 1
        elif result == 'exact_location':
            exact_location_count += 1
        elif result == 'city_match':
            city_match_count += 1
        elif result == 'country_match':
            country_match_count += 1
        elif result == 'mismatch':
            # increment the mismatch count regardless of locations being the same or different
            mismatch_count += 1
        elif result == 'error':
            print(f"Error for row {index}: {row['text']}") 

# print the counts for different match categories
print("\nMatch Categories:")
print(f"Exact Location Matches: {exact_location_count}")
print(f"City Matches: {city_match_count}")
print(f"Country Matches: {country_match_count}")

print("\nMismatch Categories:")
print(f"Total Mismatches: {mismatch_count}")  
print(f"\nNo Location Mentioned: {no_location_mentioned_count}")  

# a graph to showcase the results
labels = ['Exact Location Matches', 'City Matches', 'Country Matches',
          'Total Mismatches', 'No Location Mentioned']  
counts = [exact_location_count, city_match_count, country_match_count,
          mismatch_count, no_location_mentioned_count] 

wrapped_labels = [textwrap.fill(label, width=20) for label in labels]

fig, ax = plt.subplots()
ax.bar(wrapped_labels, counts)
ax.set_ylabel('Count')
ax.set_title('Location Match Categories')

plt.show()
