
import requests
from bs4   import BeautifulSoup as bs

git_pf = "https://github.com/Happinessprashant"

req= requests.get(git_pf)

scrapper = bs(req.content,"html.parsr")
profile_pic = scrapper.find("img" , {"alt":"Avatar"})["src"]

print(profile_pic)


# Output is :
    
#     https://avatars.githubusercontent.com/u/125643307?v=4
