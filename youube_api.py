
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pprint
import pandas as pd
import time
class YouTubeAPI:
  def __init__(self):
    # self.scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    self.scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    self.api_service_name = "youtube"
    self.api_version = "v3"
    self.client_secrets_file = "anarchy.json"

    # Get credentials and create an API client
    self.flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(self.client_secrets_file, self.scopes)
    self.credentials = self.flow.run_console()
    self.youtube = googleapiclient.discovery.build(self.api_service_name, self.api_version, credentials=self.credentials)
    
  def get_links_from_channel(self, channelId, maxResults, order, q, relevanceLanguage, videoEmbeddable, videoSyndicated):
    
    request = self.youtube.search().list(
        part="snippet",
        channelId=channelId,
        maxResults=maxResults,
        order=order,
        q=q,
        # relevanceLanguage=relevanceLanguage,
        type="video",
        videoEmbeddable=videoEmbeddable,
        videoSyndicated=videoSyndicated
    )

    response = request.execute()
    result = []
    for item in response["items"]:
      temp = []
      temp.append(item["snippet"]["channelId"])
      temp.append(item["snippet"]["channelTitle"])
      temp.append(item["snippet"]["title"])
      temp.append(item["snippet"]["description"])
      temp.append("https://www.youtube.com/watch?v=" + item["id"]["videoId"])
      result.append(temp)
    return result
# print(response)



api = YouTubeAPI()
df = pd.read_csv('topic_subtopics.csv')
# print(df.head())

# tag_names = ["pdf", "mindmaps", "videos"]
tag_names = ["video"]

journey_template_df  = []
i = 1
j = i + 25
#web search for every subtopics
for grade, subject, topic, subtopic in zip(df['Grade'], df['Subject'], df['Topic'], df['SubTopic']):
  # print(grade, topic, subtopic, subject, i, j)
  for tag in tag_names:
    if tag == "video":
      if grade == 5 and subject == "Mathematics" and i < j:
        i += 1
        print(topic, " " , subtopic)
        result = api.get_links_from_channel("UCiTjCIT_9EXV1Wp1cY0zaUA", 6, "viewCount", topic + " " + subtopic + " for class " + str(grade) + " cbse", None, "true", "true")
        print(result)
        for res in result:
          row = []
          row.append(grade)
          row.append(subject)
          row.append(topic)
          row.append(subtopic)
          row.append(tag)
          row.append(res[0])
          row.append(res[1])
          row.append(res[2])
          row.append(res[3])
          row.append(res[4])
          print(row)
          journey_template_df.append(row)
        time.sleep(10)


df = pd.DataFrame(journey_template_df, columns=["Grade", "Subject", "Topic", "SubTopic", "Tag", "channelID", "channelTitle", "title", "description", "link"])
print(df.head())
df.to_csv('resource_template_from_youtube_api_grade_5.csv', index = False)
        

      