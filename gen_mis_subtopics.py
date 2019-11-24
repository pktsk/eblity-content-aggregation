import pandas as pd


top_sub_df = pd.read_csv("maths_topics_subtopics.csv")
done_df = pd.read_csv('f1_plus_f2.csv')



final_df = []
print(len(done_df))
for i, (g1, t1, s1) in enumerate(zip(top_sub_df["Grade"], top_sub_df["Topic"], top_sub_df["SubTopic"])):
  exist = False
  temp = []
  for j, (g2, t2, s2) in enumerate(zip(done_df["Grade"], done_df["Topic"], done_df["SubTopic"])):
    if (g1 == g2 and t1 == t2 and s1 == s2):
      # print(g1, t1, s1)
      exist = True
      # print("exists")
      final_df.append([done_df["Grade"].iloc[j], done_df["Subject"].iloc[j], done_df["Topic"].iloc[j], done_df["SubTopic"].iloc[j], done_df["link"].iloc[j], done_df["tag"].iloc[j]])
      # print(done_df.loc[j])
      # final_df.append(done_df.loc[j])
  if (not exist):
    # print("doesnot exists")
    # print(g1, t1, s1)
    final_df.append([top_sub_df["Grade"].iloc[i], top_sub_df["Subject"].iloc[i], top_sub_df["Topic"].iloc[i], top_sub_df["SubTopic"].iloc[i], "", "Video"])

print(final_df[0])
new_df = pd.DataFrame(final_df, columns = done_df.columns)
# print(type(final_df))
new_df.to_csv("all_videos.csv", index=False)
print(len(final_df))
