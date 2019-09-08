from googlesearch import search 
  
# to search 
query = "Addition of 2 digit numbers filetype:pdf"
  
for j in search(query, num=5, stop=5, pause=2): 
    print(j) 