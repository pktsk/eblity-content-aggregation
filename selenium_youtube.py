from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import os
df = pd.read_csv('topic_subtopics.csv')
# set driver options
opt = Options()
opt.add_argument("--incognito")


try:
  driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=opt)
  # driver.get("https://www.youtube.com")
  # if file does not exist write header 
  if not os.path.isfile('youtube_links.csv'):
    i = 0
    j = -1
    print("file resources does not exists")
  else:  # else it exists so append without writing the header, start from the last subtopic covered
    i = 0
    temp = pd.read_csv('youtube_links.csv')
    if (len(temp) > 0):
      j = temp["index"].iloc[len(temp) - 1]
    else:
      j = 0
    print("len of df: ", j, " i: ", i)
  for grade, subject, topic, subtopic in zip(df['Grade'], df['Subject'], df['Topic'], df['SubTopic']):
    output_df = []
    print("i: ", i, " j : ", j)
    if i > j:
      # time.sleep(10)
      query = "\"" + topic + " " + subtopic + "\" for class " + str(grade) + " cbse"
      split_query = query.split(" ")
      search_query = ""
      for ind, q in enumerate(split_query):
        search_query += q
        if(ind == len(split_query) - 1):
          search_query += "+"
      # print("query: ", search_query)
      driver.get("https://www.youtube.com/results?search_query=" + query)
      # driver.find_element_by_name("search_query").clear()
      # driver.find_element_by_name("search_query").send_keys("\"" + topic + " " + subtopic + "\" for class " + str(grade) + " cbse")
      # driver.find_element_by_id("search-icon-legacy").click()
      time.sleep(10)
      WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "contents")))
      links = driver.find_elements_by_id("video-title")
      description = driver.find_elements_by_id("description-text")

      for x, description in zip(links[:10], description[:10]):
        output_df.append([grade, subject, topic, subtopic, x.get_attribute("title"), description.text, x.get_attribute("href"), i])
        print("title: ", x.get_attribute("title"))
        print("href: ", x.get_attribute("href"))
        print("description: ", description.text)
      
      # if file does not exist write header 
      if not os.path.isfile('youtube_links.csv'):
        df = pd.DataFrame(output_df, columns=["Grade", "Subject", "Topic", "SubTopic", "title", "description", "link", "index"])
        df.to_csv('youtube_links.csv', index = False)
      else:  # else it exists so append without writing the header
        print("file already exists")
        df = pd.DataFrame(output_df)
        df.to_csv('youtube_links.csv', mode='a', header=False, index = False)
    i += 1
except:
  print("exception occured")
  driver.quit()


driver.quit()
