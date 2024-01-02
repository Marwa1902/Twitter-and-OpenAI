# Twitter-and-OpenAI

# Introduction 

OpenAI API allows developers to access and integrate the capabilities of OpenAI’s languages models into applications or servies and provides a way to interact with models such as GPT-3.5, enabling users to generate human-like text, performing various language related tasks. OpenAI’s language model, including GPT – 3.5 , can analyze the content of tweets to understand the context and extract information retaled to spatial and temporal concepts. It can be used to extract location-related information from tweets, such as user locations, mentioned locations, or topics associated with specific places. This helps in understanding where the tweet is referring to spatially.

The models can also interpret and analyze timestamps, dates, and temporal expressions in tweets. This capability enables the extraction of temporal information, allowing users to understand when an event occurred or when the tweet was posted. By analyzing the content of tweets, OpenAI API can help identify the main topics or subjects being discussed which contributes to understanding the context and relevance of spatial and temporal elements within the tweet. Understanding the spatial and temporal context of tweets has become a significant
area of research in recent years. Several studies have explored locations mentioned in
tweets and accurately estimate geo-coordinates for Twitter posts using various
methodologies, combining natural language processing (NLP) and machine learning
techniques to unveil the geographical and temporal dimensions of tweets.

# Goal:
 Our primary objective was to evaluate the accuracy of users' locations mentioned in their tweets and compare it to specific locations, all extracted and analysed by OpenAI itself. We give two comparison to OpenAI’s API, topic mentioned location vs geotagged location and then user mentioned location vs the topic location (the location which the user has mentioned and is discussing about, but we do not know the location is where the user is currently in), and then label them according to their resemblance. This would help us know that any mentioned user location is accurately alike to the mentioned discussed location or geotagged location.

# Aims and Objectives
The primary aim of our research is to evaluate the accuracy of OpenAI’s location extraction capabilities when applied to tweets and to identify patterns in its performance. 

Our objectives are twofold:
1. Evaluate Accuracy of Topic (Mentioned) Location vs Geotagged Location.
      Assessing the spatial context of the user by comparing topicmentioned locations with the geotagged location. This is to match if the topic mentioned location and geotagged location are of the same spatial context.

2. Evaluate Accuracy of User-Mentioned Location vs. Topic Location
      Investigate the accuracy of OpenAI in capturing the alignment between the user’s claimed location and the location discussed in the tweet (topic location -the location the user is discussing about but is not residing in). This comparison delves into the accuracy of OpenAI in capturing the alignment between the user's claimed location and the location discussed in the tweet. To add, this use case if for the non-geotagged location.


The reason why we evaluate the findings based on two categories is because sometimes we have no geotagged location available, maybe due to “no location shared” option from the user itself. So, we ask OpenAI to look for a user mentioned location that we can use to compare it with the topic location and extract it for comparison.

The set of comparison were put into three categories:
1. (Match): classify as “Match” if the topic mentioned location and geotagged location (or user mentioned location) are of the same location
(location can be street, city and country).
2. (Mismatch): classify as “Mismatch” if the topic mentioned location and geotagged location (or user mentioned location) are of different locations.
3. No location mentioned: classify as “No location mentioned” if there are no locations extracted from the tweet.

Our analysis focused on utilizing OpenAI [13] to extract location-related information from tweets and subsequently comparing this information with geotagged location or topic location to evaluate the location the tweets containing the location based on the classification.

![image](https://github.com/Marwa1902/Twitter-and-OpenAI/assets/89301770/bbebbb39-50a5-4b6a-9f13-6f82b743a0be)


