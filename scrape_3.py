
import requests
from bs4 import BeautifulSoup

url= [
    "https://bustimings.in/msrtc/latur-jalna/amp/",
"https://bustimings.in/msrtc/jalna-satara/amp/",
"https://bustimings.in/msrtc/washim-nagpur/amp/",
"https://bustimings.in/msrtc/solapur-dhule/amp/",
"https://bustimings.in/msrtc/washim-yavatmal/amp/",
"https://bustimings.in/msrtc/dhule-nasik/amp/",
"https://bustimings.in/msrtc/nagpur-yavatmal/amp/",
"https://bustimings.in/msrtc/kolhapur-jalna/amp/"
]


for i in range(11):
    r = requests.get(url[i])
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')
  
    print(soup.find_all('table'))