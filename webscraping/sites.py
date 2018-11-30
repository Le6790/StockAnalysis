import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.google.com/search?q=dow+jones+stock&num=5&tbs=cdr:1,cd_min:10/1/2018,cd_max:10/1/2018&source=lnms&tbm=nws")
soup = BeautifulSoup(page.content)
import re
links = soup.findAll("a")
for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    url = re.split(":(?=http)",link["href"].replace("/url?q=",""))

    print(url)