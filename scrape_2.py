from plistlib import load
import pandas as pd
import ssl 
import requests
from bs4 import BeautifulSoup


ssl._create_default_https_context = ssl._create_unverified_context

tupl = (
"https://bustimings.in/msrtc/pune-dadar/amp/",
"https://bustimings.in/msrtc/shirdi-nasik/amp/",
"https://bustimings.in/msrtc/mumbai-pune/amp/",
"https://bustimings.in/msrtc/thane-solapur/amp/",
"https://bustimings.in/msrtc/sangli-satara/amp/",
"https://bustimings.in/msrtc/yavatmal-nasik/amp/",
"https://bustimings.in/msrtc/thane-nandurbar/amp/",
"https://bustimings.in/msrtc/yavatmal-pune/amp/",
"https://bustimings.in/msrtc/hingoli-jalna/amp/",
"https://bustimings.in/msrtc/osmanabad-nanded/amp/",
"https://bustimings.in/msrtc/parbhani-nagpur/amp/",
"https://bustimings.in/msrtc/solapur-yavatmal/amp/",
"https://bustimings.in/msrtc/thane-hingoli/amp/",
"https://bustimings.in/msrtc/thane-nasik-2/amp/",
"https://bustimings.in/msrtc/nanded-sangli/amp/",
"https://bustimings.in/msrtc/nanded-jalna/amp/",
"https://bustimings.in/msrtc/nasik-washim/amp/",
"https://bustimings.in/msrtc/nasik-kolhapur/amp/",
"https://bustimings.in/msrtc/wardha-latur/amp/",
"https://bustimings.in/msrtc/jalna-wardha/amp/",
"https://bustimings.in/msrtc/solapur-hingoli/amp/",
"https://bustimings.in/msrtc/satara-parbhani/amp/",
"https://bustimings.in/msrtc/parbhani-nasik/amp/",
"https://bustimings.in/msrtc/yavatmal-thane/amp/",
"https://bustimings.in/msrtc/nasik-satara/amp/",
"https://bustimings.in/msrtc/chandrapur-hingoli/amp/",
"https://bustimings.in/msrtc/sangli-latur/amp/",
"https://bustimings.in/msrtc/nagpur-hingoli/amp/",
"https://bustimings.in/msrtc/parbhani-osmanabad/amp/",
"https://bustimings.in/msrtc/sangli-nanded/amp/",
"https://bustimings.in/msrtc/jalna-sangli/amp/",
"https://bustimings.in/msrtc/sangli-parbhani/amp/",
"https://bustimings.in/msrtc/latur-jalna/amp/",
"https://bustimings.in/msrtc/jalna-satara/amp/",
"https://bustimings.in/msrtc/washim-nagpur/amp/",
"https://bustimings.in/msrtc/solapur-dhule/amp/",
"https://bustimings.in/msrtc/washim-yavatmal/amp/",
"https://bustimings.in/msrtc/dhule-nasik/amp/",
"https://bustimings.in/msrtc/nagpur-yavatmal/amp/",
"https://bustimings.in/msrtc/kolhapur-jalna/amp/",
"https://bustimings.in/msrtc/solapur-osmanabad/amp/",
"https://bustimings.in/msrtc/latur-kolhapur/amp/",
"https://bustimings.in/msrtc/wardha-washim/amp/",
"https://bustimings.in/msrtc/washim-wardha/amp/",
"https://bustimings.in/msrtc/parbhani-jalna/amp/",
"https://bustimings.in/msrtc/jalna-solapur/amp/",
"https://bustimings.in/msrtc/washim-nasik/amp/",
"https://bustimings.in/msrtc/osmanabad-sangli/amp/",
"https://bustimings.in/msrtc/hingoli-nasik/amp/",
"https://bustimings.in/msrtc/hingoli-wardha/amp/",
"https://bustimings.in/msrtc/dhule-shirdi/amp/",
"https://bustimings.in/msrtc/shirdi-sangli/amp/",
"https://bustimings.in/msrtc/osmanabad-dhule/amp/",
"https://bustimings.in/msrtc/osmanabad-latur/amp/",
"https://bustimings.in/msrtc/yavatmal-nagpur/amp/",
"https://bustimings.in/msrtc/yavatmal-parbhani/amp/",
"https://bustimings.in/msrtc/shirdi-latur/amp/",
"https://bustimings.in/msrtc/parbhani-sangli/amp/",
"https://bustimings.in/msrtc/nanded-wardha/amp/",
"https://bustimings.in/msrtc/osmanabad-nagpur/amp/",
"https://bustimings.in/msrtc/washim-shirdi/amp/",
"https://bustimings.in/msrtc/washim-latur/amp/",
"https://bustimings.in/msrtc/osmanabad-solapur/amp/",
"https://bustimings.in/msrtc/dhule-pune/amp/",
"https://bustimings.in/msrtc/latur-yavatmal/amp/",
"https://bustimings.in/msrtc/parbhani-hingoli/amp/",
"https://bustimings.in/msrtc/parbhani-satara/amp/",
"https://bustimings.in/msrtc/satara-ratnagiri/amp/",
"https://bustimings.in/msrtc/jalna-parbhani/amp/",
"https://bustimings.in/msrtc/latur-shirdi/amp/",
"https://bustimings.in/msrtc/satara-nanded/amp/",
"https://bustimings.in/msrtc/jalna-washim/amp/",
"https://bustimings.in/msrtc/gadchiroli-chandrapur/amp/",
"https://bustimings.in/msrtc/ratnagiri-satara/amp/",
"https://bustimings.in/msrtc/kolhapur-sangli/amp/",
"https://bustimings.in/msrtc/washim-hingoli/amp/",
"https://bustimings.in/msrtc/washim-pune/amp/",
"https://bustimings.in/msrtc/latur-parbhani/amp/",
"https://bustimings.in/msrtc/solapur-ratnagiri/amp/",
"https://bustimings.in/msrtc/satara-kolhapur/amp/",
"https://bustimings.in/msrtc/kolhapur-thane/amp/",
"https://bustimings.in/msrtc/solapur-nanded/amp/",
"https://bustimings.in/msrtc/latur-satara/amp/",
"https://bustimings.in/msrtc/thane-pune/amp/",
"https://bustimings.in/msrtc/latur-ratnagiri/amp/",
"https://bustimings.in/msrtc/yavatmal-washim/amp/",
"https://bustimings.in/msrtc/sangli-jalna/amp/",
"https://bustimings.in/msrtc/parbhani-nanded/amp/",
"https://bustimings.in/msrtc/palghar-pune/amp/",
"https://bustimings.in/msrtc/thane-sangli/amp/",
"https://bustimings.in/msrtc/satara-nasik/amp/",
"https://bustimings.in/msrtc/pune-washim/amp/",
"https://bustimings.in/msrtc/dhule-yavatmal/amp/",
"https://bustimings.in/msrtc/nasik-hingoli/amp/",
"https://bustimings.in/msrtc/wardha-nanded/amp/",
"https://bustimings.in/msrtc/parbhani-pune/amp/",
"https://bustimings.in/msrtc/solapur-wardha/amp/",
"https://bustimings.in/msrtc/yavatmal-to-wardha/amp/",
"https://bustimings.in/msrtc/pune-hingoli/amp/",
"https://bustimings.in/msrtc/thane-nasik/amp/",
"https://bustimings.in/msrtc/osmanabad-pune/amp/",
)

for i in range(101):
    url = tupl[i]
    htm_l = requests.get(url).content
    df_list = pd.read_html(htm_l) 

    df = df_list[-1]
    print(df)
    df.to_csv('output.csv')





# for i in range(101):

#     scraper = pd.read_html(tupl[i].format(i))
#     print(scraper)
