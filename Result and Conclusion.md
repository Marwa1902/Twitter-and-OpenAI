# Results 
The results attained are displayed in the terminal as well as statistical techniques such as visualization with Matplotlib. 

After running the dataset, the number of mismatches were enormous, so we studied the results by examining the csv file, and running it again on a smaller sample, size of 110, as well as understanding the OpenAI partake in this outcome.

Mismatch:
1. Location same as geotag but mismatch by OpenAI – 41 -37.27%
2. Location different as geotag and mismatch by OpenAI – 4 - 3.64%
3. No Location mentioned but mismatch by OpenAI – 21 - 19.09%


  ![Figure_1](https://github.com/Marwa1902/Twitter-and-OpenAI/assets/89301770/491d787e-f373-46e7-9054-8daa40c30325)


In the above statistics, the samples of the dataset were to see the accuracy of the mismatches in the previous experiments we had done. Running the experiment a few times and taking different samples, size of 110, each time, we took a set of results from each sample and focusing only on mismatches (we had matches and no location mentioned in the results) we came up with those numbers.


The 3 categories of Mismatch are as follows:
1. The topic location extracted by the OpenAI is compared to the geotagged location, and although both the locations match, the result of the comparison by OpenAI was a mismatch.
2. The topic location extracted by the OpenAI is compared to the geotagged location, and the locations do not match, and the result of the comparison by OpenAI was a mismatch.
3. The topic location was not mentioned in the tweet text and the OpenAI did not retrieve any location (topic_location = UNKNOWN) but the OpenAI still compared it with geotagged location and gave an output as mismatch.

A reason for category (1) to occur might be one of 2 reasons:
1. The retrieved locations from the tweet text are in abbreviations.
   
• Example (1):
Original Tweet:
This job is now open at Lowes in #Epping NH Follow us
and turn on mobile alerts to hear about jobs like these as…
Detailed Response:
User Location: Unknown
Mentioned Location: Epping, NH, USA
Country: USA
City: Epping
Mentioned Location (from text): Epping, NH, USA
Geolocation (from latitude and longitude): Lowe's, 36,
Fresh River Road, Epping Crossing, Epping, Rockingham
County, New Hampshire, 03042, United States
Mismatch: Mentioned location does not match geolocation

• Example (2) :
Original Tweet:
Can you recommend anyone for this job in #Stanardsville
VA #Transportation
Detailed Response:
User's Location: Unknown
Mentioned Location: Stanardsville, VA, United States
Country: United States
City: Stanardsville
Mentions: #Stanardsville VA #Transportation
Mentioned Location (from text): Stanardsville, VA, United States
Geolocation (from latitude and longitude): Judges Road,
Stanardsville,
Greene County, Virginia, 22973, United States
Mismatch: Mentioned location does not match geolocation

3. The geotagged location is too specific.
   
• Example
Original Tweet:
Want to work at Leander ISD Were hiring in #Leander TX!
Click the link in our bio for details on this job and mo…
Detailed Response:
User Location: Unknown
Mentioned Location: Leander, TX, United States
Country: United States
City: Leander
Mentions: Leander ISD
Mentioned Location (from text): Leander, TX, United States
Geolocation (from latitude and longitude): Leander's
Inspection Connection, 101, West South Street, Westview
Meadows, Leander, Williamson County, Texas, 78641, United
States
Mismatch: Mentioned location does not match geolocation
Regarding category (3), there is 1 reason why it compares with geotagged
even when the location is not mentioned. The OpenAI did not retrieve the
location as it is not mentioned in the tweet, so sometimes it returns ‘None’
instead of ‘Unknown’, where it thinks ‘None’ is a location and compares
them.

• Example (1):
Original Tweet:
Weekly Specials Worn 2016 Air Jordan 1 Retro High Black
Toe #65756 Sz 10 w Replacement Box In Great Condition A…
Detailed Response:
User Location: Unknown
Mentioned Location: None
Country: Unknown
City: Unknown
Date: Unknown
Time: Unknown
Events: None
Mentions: None
Mentioned Location (from text): None
Geolocation (from latitude and longitude): 1201, Lincoln
Avenue, Alameda, Alameda County, California, 94501, United
States
Mismatch: Mentioned location does not match geolocation

• Example (2) :
Original Tweet:
Always love tattooing roses Thank you Christian! #rose #roses
#redrose #tattoo #tattoos #flower…
Detailed Response:
User Location: Unknown
Mentioned Location: None
Country: Unknown
City: Unknown
Date: Unknown
Time: Unknown
Events: None
Mentions: Christian
Mentioned Location (from text): None
Geolocation (from latitude and longitude): 568, South Norfolk
Street, San Mateo, San Mateo County, California, 94401,
United States
Mismatch: Mentioned location does not match geolocation

When it returns ‘Unknown’, then it does not compare it and returns ‘No location mentioned’.

There were a lot of challenges faced during the test phase. These challenges were crucial to the inaccuracies in user-mentioned locations, variations in geotagged information accuracy and the interpretation of topic locations. 

The main challenge was that in most cases, OpenAI was unable to detect the locations and would result in an output that was not accurate.

For example, the following output, the geolocation, and user mentioned location are same, but it still classifies it as “Mentioned Location does not match geolocation”. This could be due to the abbreviation and the accuracy of the specific location, so it picks it up as mismatch.

  ![image](https://github.com/Marwa1902/Twitter-and-OpenAI/assets/89301770/e0a5763d-336b-497f-b6aa-61fa04ed1689)

To tackle these challenges, we applied validation of the tweet data that is implemented by cross checking the information with the csv file manually as well as running as many samples as possible to get tweets that are more detailed for the model to understand it.

# Conclusion 
In conclusion, the analysis brings the importance of location extraction results, understanding the types of mismatches and why it occurred and identified limitations highlight potential areas for improvement in OpenAI’s location extraction and capabilities.
Although OpenAI excelled in most cases in extracting locations based on the objectives given to it to analyze, in other cases it failed to identify locations as it detected simple objects as locations or sometimes did not even extract locations even though there were mentioned of locations. To these results, we come to conclude that only using OpenAI might have a missing ability to get location if the tweet is not detailed enough. 
