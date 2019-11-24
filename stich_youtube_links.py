import pandas as pd

top_sub_df = pd.read_csv('maths_topics_subtopics.csv')
rev1_df = pd.read_csv('rev_links1.csv')
rev2_df = pd.read_csv('rev_links2.csv')

resources = []
# for grade, subject, topic, subtopic in zip(top_sub_df['Grade'], top_sub_df['Subject'], top_sub_df['Topic'], top_sub_df['SubTopic']):
#   if subject == "Mathematics":
for g1, s1, t1, sub1, remark, link1 in zip(rev1_df["Grade"], rev1_df['Subject'], rev1_df['Topic'], rev1_df['SubTopic'], rev1_df['Remark'], rev1_df['link']):
  if s1 == "Mathematics" and type(remark) == type("") and (remark.find("Approved") != -1 or remark.find("Relevant") != -1 or remark.find("Relevent") != -1):
    resources.append([g1, s1, t1, sub1, link1, "Video"])
  else:
    for g2, s2, t2, sub2, link2 in zip(rev2_df["Grade"], rev2_df["Subject"], rev2_df["Topic"], rev2_df["SubTopic"], rev2_df["link"]):
      if g1 == g2 and s2 == "Mathematics" and t2 == t1 and sub1 == sub2:
        resources.append([g2, s2, t2, sub2, link2, "Video"])
      # else:
      #   if s2 == "Mathematics":
      #     resources.append([g1, s2, t1, sub1, "", "Video"])

# print(resources)
new_df = pd.DataFrame(resources, columns=["Grade", "Subject", "Topic", "SubTopic", "link", "tag"])
new_df.to_csv("f1_plus_f2.csv", index = False)
# print(new_df.head(10))
# columns = top_sub_df.columns
# print(columns[0])
# print(new_df.head(10))

# i = 0
# j = 0
# print(len(new_df))

# final_df = []
# while (i != len(top_sub_df)):
#   print(f"i: {i} -----  j : {j}")
#   if(top_sub_df["Subject"].iloc[i] == "Mathematics"):
#     if (top_sub_df["Grade"].iloc[i] == new_df["Grade"].iloc[j]) and (top_sub_df["Subject"].iloc[i] == new_df["Subject"].iloc[j]) and (top_sub_df["Topic"].iloc[i] == new_df["Topic"].iloc[j]) and (top_sub_df["SubTopic"].iloc[i] == new_df["SubTopic"].iloc[j]):
#       final_df.append(new_df.loc[j])
#       j += 1
#       print(f"i: {i} -----  j : {j}")
#     else:
#       i += 1
#       if i >= len(top_sub_df):
#         break
#       print(f"i: {i} -----  j : {j}")
#       if(top_sub_df["Subject"].iloc[i] == "Mathematics"):
#         if (top_sub_df["Grade"].iloc[i] != new_df["Grade"].iloc[j]) and (top_sub_df["Subject"].iloc[i] != new_df["Subject"].iloc[j]) and (top_sub_df["Topic"].iloc[i] != new_df["Topic"].iloc[j]) and (top_sub_df["SubTopic"].iloc[i] != new_df["SubTopic"].iloc[j]):
#           final_df.append([top_sub_df["Grade"].iloc[i], top_sub_df["Subject"].iloc[i], top_sub_df["Topic"].iloc[i], top_sub_df["SubTopic"].iloc[i], "", "Video"])
#   else:
#     i += 1

# print(final_df)
# df = pd.DataFrame(final_df)
# df.to_csv("resources_videos.csv", index = False)


