
import requests
from bs4   import BeautifulSoup as bs

gitpf = "https://github.com/Happinessprashant"

req= requests.get(gitpf)

scrapper = bs(req.content,"html.parser")
profile_pic = scrapper.find("img" , {"alt":"Avatar"})["src"]

print(profile_pic)


# Output is :
    
#     https://avatars.githubusercontent.com/u/125643307?v=4
