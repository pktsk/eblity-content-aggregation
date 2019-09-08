from googlesearch import search
import pandas as pd

#read topic subtopic table
df = pd.read_csv('topic_subtopics.csv')
# print(df.head())

tag_names = ["pdf", "mindmaps", "videos"]

journey_template_df  = []
#web search for every subtopics
for grade, topic, subtopic in zip(df['Grade'], df['Topic'], df['SubTopic']):
    # web_search_query = "grade " + str(grade) + " topic " + topic + " subtopic " + subtopic
    web_search_query = "grade " + str(grade) + " " + subtopic
    # web_search_query = subtopic
    # search for every tags
    for tag in tag_names:

        if tag == "pdf":
            query = web_search_query + " filetype:pdf"
        elif tag == "mindmaps":
            query = web_search_query + " mindmaps filetype:pdf"
        else:
            query = web_search_query + " site:www.youtube.com"
        # print(query)
        for link in search(query, num=10, stop=5, pause=2):
            # print(link)
            row = []
            row.append(grade)
            row.append(df['Subject'].iloc[0])
            row.append(topic)
            row.append(subtopic)
            row.append(tag)
            row.append(link)
            print(row)
            journey_template_df.append(row)
    # break

# print(journey_template_df[0])
df = pd.DataFrame(journey_template_df, columns=["Grade", "Subject", "Topic", "Sub Topic", "Tag", "Link"])
df.to_csv('resource_template.csv', index = False, )
        

