import requests
from bs4 import BeautifulSoup

url = [
# "https://bustimings.in/msrtc/solapur-osmanabad/amp/",
# "https://bustimings.in/msrtc/latur-kolhapur/amp/",
# "https://bustimings.in/msrtc/wardha-washim/amp/",
# "https://bustimings.in/msrtc/washim-wardha/amp/",
# "https://bustimings.in/msrtc/parbhani-jalna/amp/",
# "https://bustimings.in/msrtc/jalna-solapur/amp/",
# "https://bustimings.in/msrtc/washim-nasik/amp/",
# "https://bustimings.in/msrtc/osmanabad-sangli/amp/",
# "https://bustimings.in/msrtc/hingoli-nasik/amp/",
# "https://bustimings.in/msrtc/hingoli-wardha/amp/",
# "https://bustimings.in/msrtc/dhule-shirdi/amp/",
# "https://bustimings.in/msrtc/shirdi-sangli/amp/",
# "https://bustimings.in/msrtc/osmanabad-dhule/amp/",
# "https://bustimings.in/msrtc/osmanabad-latur/amp/",
# "https://bustimings.in/msrtc/yavatmal-nagpur/amp/",
# "https://bustimings.in/msrtc/yavatmal-parbhani/amp/",
# "https://bustimings.in/msrtc/shirdi-latur/amp/",
# "https://bustimings.in/msrtc/parbhani-sangli/amp/",
# "https://bustimings.in/msrtc/nanded-wardha/amp/",
# "https://bustimings.in/msrtc/osmanabad-nagpur/amp/",
# "https://bustimings.in/msrtc/washim-shirdi/amp/",
# "https://bustimings.in/msrtc/washim-latur/amp/",
# "https://bustimings.in/msrtc/osmanabad-solapur/amp/",
# "https://bustimings.in/msrtc/dhule-pune/amp/",
# "https://bustimings.in/msrtc/latur-yavatmal/amp/",
# "https://bustimings.in/msrtc/parbhani-hingoli/amp/",
# "https://bustimings.in/msrtc/parbhani-satara/amp/",
# "https://bustimings.in/msrtc/satara-ratnagiri/amp/",
# "https://bustimings.in/msrtc/jalna-parbhani/amp/",
# "https://bustimings.in/msrtc/latur-shirdi/amp/",
# "https://bustimings.in/msrtc/satara-nanded/amp/",
# "https://bustimings.in/msrtc/jalna-washim/amp/",
# "https://bustimings.in/msrtc/gadchiroli-chandrapur/amp/",
# "https://bustimings.in/msrtc/ratnagiri-satara/amp/",
# "https://bustimings.in/msrtc/kolhapur-sangli/amp/",
# "https://bustimings.in/msrtc/washim-hingoli/amp/",
# "https://bustimings.in/msrtc/washim-pune/amp/",
# "https://bustimings.in/msrtc/latur-parbhani/amp/",
# "https://bustimings.in/msrtc/solapur-ratnagiri/amp/",
# "https://bustimings.in/msrtc/satara-kolhapur/amp/",
# "https://bustimings.in/msrtc/kolhapur-thane/amp/",
# "https://bustimings.in/msrtc/solapur-nanded/amp/",
# "https://bustimings.in/msrtc/latur-satara/amp/",
# "https://bustimings.in/msrtc/thane-pune/amp/",
# "https://bustimings.in/msrtc/latur-ratnagiri/amp/",
# "https://bustimings.in/msrtc/yavatmal-washim/amp/",
# "https://bustimings.in/msrtc/sangli-jalna/amp/",
# "https://bustimings.in/msrtc/parbhani-nanded/amp/",
# "https://bustimings.in/msrtc/palghar-pune/amp/",
# "https://bustimings.in/msrtc/thane-sangli/amp/",
# "https://bustimings.in/msrtc/satara-nasik/amp/",
# "https://bustimings.in/msrtc/pune-washim/amp/",
# "https://bustimings.in/msrtc/dhule-yavatmal/amp/",
# "https://bustimings.in/msrtc/nasik-hingoli/amp/",
# "https://bustimings.in/msrtc/wardha-nanded/amp/",
# "https://bustimings.in/msrtc/parbhani-pune/amp/",
# "https://bustimings.in/msrtc/solapur-wardha/amp/",
# "https://bustimings.in/msrtc/yavatmal-to-wardha/amp/",
# "https://bustimings.in/msrtc/pune-hingoli/amp/",
# "https://bustimings.in/msrtc/thane-nasik/amp/",
# "https://bustimings.in/msrtc/osmanabad-pune/amp/",
# "https://bustimings.in/msrtc/nandurbar-nasik/amp/",
# "https://bustimings.in/msrtc/thane-dhule/amp/",
# "https://bustimings.in/msrtc/sangli-ratnagiri/amp/",
# "https://bustimings.in/msrtc/ratnagiri-sangli/amp/",
# "https://bustimings.in/msrtc/nanded-washim/amp/",
# "https://bustimings.in/msrtc/nasik-thane/amp/",
# "https://bustimings.in/msrtc/sangli-thane/amp/",
# "https://bustimings.in/msrtc/solapur-shirdi/amp/",
# "https://bustimings.in/msrtc/nanded-yavatmal/amp/",
# "https://bustimings.in/msrtc/latur-hingoli/amp/",
# "https://bustimings.in/msrtc/washim-dhule/amp/",
# "https://bustimings.in/msrtc/solapur-satara/amp/",
# "https://bustimings.in/msrtc/sangli-shirdi/amp/",
# "https://bustimings.in/msrtc/satara-solapur/amp/",
# "https://bustimings.in/msrtc/parbhani-thane/amp/",
# "https://bustimings.in/msrtc/sangli-nasik/amp/",
# "https://bustimings.in/msrtc/jalna-shirdi/amp/",
# "https://bustimings.in/msrtc/yavatmal-jalna/amp/",
# "https://bustimings.in/msrtc/solapur-thane/amp/",
# "https://bustimings.in/msrtc/hingoli-nagpur/amp/",
# "https://bustimings.in/msrtc/yavatmal-dhule/amp/",
# "https://bustimings.in/msrtc/washim-parbhani/amp/",
# "https://bustimings.in/msrtc/parbhani-kolhapur/amp/",
# "https://bustimings.in/msrtc/sangli-solapur/amp/",
# "https://bustimings.in/msrtc/jalna-pune/amp/",
# "https://bustimings.in/msrtc/washim-nanded/amp/",
# "https://bustimings.in/msrtc/wardha-nagpur/amp/",
# "https://bustimings.in/msrtc/wardha-yavatmal/amp/",
# "https://bustimings.in/msrtc/nanded-satara/amp/",
# "https://bustimings.in/msrtc/shirdi-dhule/amp/",
# "https://bustimings.in/msrtc/thane-shirdi/amp/",
# "https://bustimings.in/msrtc/satara-latur/amp/",
# "https://bustimings.in/msrtc/pune-yavatmal/amp/",
# "https://bustimings.in/msrtc/shirdi-jalna/amp/",
# "https://bustimings.in/msrtc/parbhani-chandrapur/amp/",
# "https://bustimings.in/msrtc/jalna-osmanabad/amp/",
# "https://bustimings.in/msrtc/nandurbar-pune/amp/",
# "https://bustimings.in/msrtc/parbhani-yavatmal/amp/",
# "https://bustimings.in/msrtc/nasik-jalna/amp/",
# "https://bustimings.in/msrtc/hingoli-pune/amp/",
# "https://bustimings.in/msrtc/jalna-nagpur/amp/",
# "https://bustimings.in/msrtc/solapur-jalna/amp/",
# "https://bustimings.in/msrtc/pune-nanded/amp/",
# "https://bustimings.in/msrtc/washim-jalna/amp/",
# "https://bustimings.in/msrtc/nagpur-jalna/amp/",
# "https://bustimings.in/msrtc/kolhapur-osmanabad/amp/",
# "https://bustimings.in/msrtc/yavatmal-nanded/amp/",
# "https://bustimings.in/msrtc/nasik-pune/amp/",
# "https://bustimings.in/msrtc/solapur-sangli/amp/",
# "https://bustimings.in/msrtc/dhule-parbhani/amp/",
# "https://bustimings.in/msrtc/parbhani-latur/amp/",
# "https://bustimings.in/msrtc/satara-thane/amp/",
# "https://bustimings.in/msrtc/thane-ratnagiri/amp/",
# "https://bustimings.in/msrtc/latur-nagpur/amp/",
# "https://bustimings.in/msrtc/solapur-nasik/amp/",
# "https://bustimings.in/msrtc/pune-satara/amp/",
# "https://bustimings.in/msrtc/solapur-latur/amp/",
# "https://bustimings.in/msrtc/nanded-chandrapur/amp/",
# "https://bustimings.in/msrtc/satara-pune/amp/",
# "https://bustimings.in/msrtc/yavatmal-latur/amp/",
# "https://bustimings.in/msrtc/sangli-kolhapur/amp/",
# "https://bustimings.in/msrtc/nanded-solapur/amp/",
# "https://bustimings.in/msrtc/solapur-kolhapur/amp/",
# "https://bustimings.in/msrtc/ratnagiri-pune/amp/",
# "https://bustimings.in/msrtc/chandrapur-nagpur/amp/",
# "https://bustimings.in/msrtc/nagpur-wardha/amp/",
# "https://bustimings.in/msrtc/solapur-pune/amp/",
# "https://bustimings.in/msrtc/sangli-pune/amp/",
# "https://bustimings.in/msrtc/latur-nanded/amp/",
# "https://bustimings.in/msrtc/chandrapur-gadchiroli/amp/",
# "https://bustimings.in/msrtc/nanded-latur/amp/",
# "https://bustimings.in/msrtc/kolhapur-pune/amp/",
# "https://bustimings.in/msrtc/nasik-nandurbar/amp/",
# "https://bustimings.in/msrtc/pune-kolhapur/amp/",
# "https://bustimings.in/msrtc/pune-jalna/amp/",
# "https://bustimings.in/msrtc/pune-osmanabad/amp/",
# "https://bustimings.in/msrtc/pune-ratnagiri/amp/",
# "https://bustimings.in/msrtc/pune-parbhani/amp/",
# "https://bustimings.in/msrtc/pune-solapur/amp/",
# "https://bustimings.in/msrtc/pune-dhule/amp/",
# "https://bustimings.in/msrtc/kolhapur-ratnagiri/amp/",
# "https://bustimings.in/msrtc/pune-latur/amp/",
# "https://bustimings.in/msrtc/ratnagiri-kolhapur/amp/",
# "https://bustimings.in/msrtc/shirdi-washim/amp/",
# "https://bustimings.in/msrtc/shirdi-pune/amp/",
# "https://bustimings.in/msrtc/osmanabad-shirdi/amp/",
# "https://bustimings.in/msrtc/palghar-nasik/amp/",
# "https://bustimings.in/msrtc/osmanabad-parbhani/amp/",
# "https://bustimings.in/msrtc/osmanabad-nasik/amp/",
# "https://bustimings.in/msrtc/osmanabad-kolhapur/amp/",
# "https://bustimings.in/msrtc/osmanabad-jalna/amp/",
# "https://bustimings.in/msrtc/nasik-yavatmal/amp/",
# "https://bustimings.in/msrtc/nasik-solapur/amp/",
# "https://bustimings.in/msrtc/nasik-sangli/amp/",
# "https://bustimings.in/msrtc/nasik-palghar/amp/",
# "https://bustimings.in/msrtc/nandurbar-shirdi/amp/",
# "https://bustimings.in/msrtc/nanded-pune/amp/",
# "https://bustimings.in/msrtc/nanded-osmanabad/amp/",
# "https://bustimings.in/msrtc/nanded-nagpur/amp/",
# "https://bustimings.in/msrtc/nanded-hingoli/amp/",
# "https://bustimings.in/msrtc/nagpur-washim/amp/",
# "https://bustimings.in/msrtc/nagpur-solapur/amp/",
# "https://bustimings.in/msrtc/nagpur-parbhani/amp/",
# "https://bustimings.in/msrtc/nagpur-nanded/amp/",
# "https://bustimings.in/msrtc/nagpur-latur/amp/",
# "https://bustimings.in/msrtc/nagpur-chandrapur/amp/",
# "https://bustimings.in/msrtc/mumbai-central-solapur/amp/",
# "https://bustimings.in/msrtc/latur-washim/amp/",
# "https://bustimings.in/msrtc/latur-wardha/amp/",
# "https://bustimings.in/msrtc/latur-solapur/amp/",
# "https://bustimings.in/msrtc/latur-sangli/amp/",
# "https://bustimings.in/msrtc/latur-pune/amp/"

# "https://bustimings.in/msrtc/latur-osmanabad/amp/",
# "https://bustimings.in/msrtc/latur-nasik/amp/",
# "https://bustimings.in/msrtc/kolhapur-solapur/amp/",
# "https://bustimings.in/msrtc/kolhapur-parbhani/amp/",
# "https://bustimings.in/msrtc/kolhapur-nasik/amp/",
# "https://bustimings.in/msrtc/kolhapur-nanded/amp/",
# "https://bustimings.in/msrtc/jalna-nasik/amp/",
# "https://bustimings.in/msrtc/jalna-nanded/amp/",
# "https://bustimings.in/msrtc/jalna-latur/amp/",
# "https://bustimings.in/msrtc/jalna-hingoli/amp/",
# "https://bustimings.in/msrtc/jalna-dhule/amp/",
# "https://bustimings.in/msrtc/hingoli-yavatmal/amp/",
# "https://bustimings.in/msrtc/hingoli-washim/amp/",
# "https://bustimings.in/msrtc/hingoli-solapur/amp/",
# "https://bustimings.in/msrtc/hingoli-parbhani/amp/",
# "https://bustimings.in/msrtc/hingoli-nanded/amp/",
# "https://bustimings.in/msrtc/dhule-solapur/amp/",
# "https://bustimings.in/msrtc/pune-chandrapur/amp/",
# "https://bustimings.in/msrtc/chandrapur-pune/amp/",
# "https://bustimings.in/msrtc/shirdi-chandrapur/amp/",
# "https://bustimings.in/msrtc/wardha-chandrapur/amp/",
# "https://bustimings.in/msrtc/chandrapur-wardha/amp/",
# "https://bustimings.in/msrtc/chandrapur-washim/amp/",
# "https://bustimings.in/msrtc/washim-chandrapur/amp/",
# "https://bustimings.in/msrtc/yavatmal-chandrapur/amp/",
# "https://bustimings.in/msrtc/chandrapur-yavatmal/amp/",
# "https://bustimings.in/msrtc/bhandara-yavatmal/amp/",
# "https://bustimings.in/msrtc/yavatmal-bhandara/amp/",
# "https://bustimings.in/msrtc/washim-bhandara/amp/",
# "https://bustimings.in/msrtc/bhandara-washim/amp/",
# "https://bustimings.in/msrtc/bhandara-wardha/amp/",
# "https://bustimings.in/msrtc/wardha-bhandara/amp/",
# "https://bustimings.in/msrtc/nagpur-bhandara/amp/",
# "https://bustimings.in/msrtc/bhandara-nagpur/amp/",
# "https://bustimings.in/msrtc/bhandara-gondia/amp/",
# "https://bustimings.in/msrtc/gondia-bhandara/amp/",
# "https://bustimings.in/msrtc/chandrapur-bhandara/amp/",
# "https://bustimings.in/msrtc/bhandara-chandrapur/amp/",
# "https://bustimings.in/msrtc/solapur-beed/amp/",
# "https://bustimings.in/msrtc/beed-solapur/amp/",
# "https://bustimings.in/msrtc/beed-satara/amp/",
# "https://bustimings.in/msrtc/satara-beed/amp/",
# "https://bustimings.in/msrtc/sangli-beed/amp/",
# "https://bustimings.in/msrtc/beed-sangli/amp/",
# "https://bustimings.in/msrtc/beed-pune/amp/",
# "https://bustimings.in/msrtc/pune-beed/amp/",
# "https://bustimings.in/msrtc/parbhani-beed/amp/",
# "https://bustimings.in/msrtc/beed-parbhani/amp/",
# "https://bustimings.in/msrtc/beed-osmanabad/amp/",
# "https://bustimings.in/msrtc/osmanabad-beed/amp/",
# "https://bustimings.in/msrtc/nanded-beed/amp/",
# "https://bustimings.in/msrtc/beed-nanded/amp/",
# "https://bustimings.in/msrtc/beed-latur/amp/",
# "https://bustimings.in/msrtc/latur-beed/amp/",
# "https://bustimings.in/msrtc/kolhapur-beed/amp/",
# "https://bustimings.in/msrtc/beed-kolhapur/amp/",
# "https://bustimings.in/msrtc/beed-jalna/amp/",
# "https://bustimings.in/msrtc/jalna-beed/amp/",
# "https://bustimings.in/msrtc/hingoli-beed/amp/",
# "https://bustimings.in/msrtc/beed-hingoli/amp/",
# "https://bustimings.in/msrtc/beed-dhule/amp/",
# "https://bustimings.in/msrtc/dhule-beed/amp/",
# "https://bustimings.in/msrtc/buldhana-beed/amp/",
# "https://bustimings.in/msrtc/beed-buldhana/amp/",
# "https://bustimings.in/msrtc/beed-mumbai/amp/",
# "https://bustimings.in/msrtc/mumbai-beed/amp/",
# "https://bustimings.in/msrtc/mumbai-dhule/amp/",
# "https://bustimings.in/msrtc/dhule-mumbai/amp/",
# "https://bustimings.in/msrtc/mumbai-hingoli/amp/",
# "https://bustimings.in/msrtc/hingoli-mumbai/amp/",
# "https://bustimings.in/msrtc/jalna-mumbai/amp/",
# "https://bustimings.in/msrtc/mumbai-jalna/amp/",
# "https://bustimings.in/msrtc/mumbai-kolhapur/amp/",
# "https://bustimings.in/msrtc/kolhapur-mumbai/amp/",
# "https://bustimings.in/msrtc/latur-mumbai/amp/",
# "https://bustimings.in/msrtc/mumbai-latur/amp/",
# "https://bustimings.in/msrtc/mumbai-nanded/amp/",
# "https://bustimings.in/msrtc/nanded-mumbai/amp/",
# "https://bustimings.in/msrtc/nandurbar-mumbai/amp/",
# "https://bustimings.in/msrtc/mumbai-nandurbar/amp/",
# "https://bustimings.in/msrtc/mumbai-osmanabad/amp/",
# "https://bustimings.in/msrtc/osmanabad-mumbai/amp/",
# "https://bustimings.in/msrtc/parbhani-mumbai/amp/",
# "https://bustimings.in/msrtc/mumbai-parbhani/amp/",
# "https://bustimings.in/msrtc/pune-mumbai/amp/",
# "https://bustimings.in/msrtc/ratnagiri-mumbai/amp/",
# "https://bustimings.in/msrtc/mumbai-ratnagiri/amp/",
# "https://bustimings.in/msrtc/mumbai-satara/amp/",
# "https://bustimings.in/msrtc/satara-mumbai/amp/",
# "https://bustimings.in/msrtc/shirdi-mumbai/amp/",
# "https://bustimings.in/msrtc/mumbai-shirdi/amp/",
# "https://bustimings.in/msrtc/mumbai-solapur/amp/",
# "https://bustimings.in/msrtc/solapur-mumbai/amp/",
# "https://bustimings.in/msrtc/yavatmal-mumbai/amp/",
# "https://bustimings.in/msrtc/mumbai-yavatmal/amp/",
# "https://bustimings.in/msrtc/aurangabad-yavatmal/amp/",
# "https://bustimings.in/msrtc/yavatmal-aurangabad/amp/",
# "https://bustimings.in/msrtc/washim-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-washim/amp/",
# "https://bustimings.in/msrtc/aurangabad-wardha/amp/",
# "https://bustimings.in/msrtc/wardha-aurangabad/amp/",
# "https://bustimings.in/msrtc/thane-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-thane/amp/",
# "https://bustimings.in/msrtc/aurangabad-solapur/amp/",
# "https://bustimings.in/msrtc/solapur-aurangabad/amp/",
# "https://bustimings.in/msrtc/shirdi-aurangabad/amp/",

# "https://bustimings.in/msrtc/aurangabad-shirdi/amp/",
# "https://bustimings.in/msrtc/aurangabad-satara/amp/",
# "https://bustimings.in/msrtc/satara-aurangabad/amp/",
# "https://bustimings.in/msrtc/sangli-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-sangli/amp/",
# "https://bustimings.in/msrtc/aurangabad-pune/amp/",
# "https://bustimings.in/msrtc/pune-aurangabad/amp/",
# "https://bustimings.in/msrtc/parbhani-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-parbhani/amp/",
# "https://bustimings.in/msrtc/aurangabad-osmanabad/amp/",
# "https://bustimings.in/msrtc/osmanabad-aurangabad/amp/",
# "https://bustimings.in/msrtc/nasik-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-nasik/amp/",
# "https://bustimings.in/msrtc/aurangabad-nandurbar/amp/",
# "https://bustimings.in/msrtc/nandurbar-aurangabad/amp/",
# "https://bustimings.in/msrtc/nanded-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-nanded/amp/",
# "https://bustimings.in/msrtc/aurangabad-nagpur/amp/",
# "https://bustimings.in/msrtc/nagpur-aurangabad/amp/",
# "https://bustimings.in/msrtc/mumbai-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-mumbai/amp/",
# "https://bustimings.in/msrtc/latur-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-latur/amp/",
# "https://bustimings.in/msrtc/kolhapur-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-kolhapur/amp/",
# "https://bustimings.in/msrtc/aurangabad-jalna/amp/"

# "https://bustimings.in/msrtc/jalna-aurangabad/amp/",
# "https://bustimings.in/msrtc/jalgoan-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-jalgaon/amp/",
# "https://bustimings.in/msrtc/aurangabad-hingoli/amp/",
# "https://bustimings.in/msrtc/hingoli-aurangabad/amp/",
# "https://bustimings.in/msrtc/dhule-aurangabad/amp/",
# "https://bustimings.in/msrtc/aurangabad-dhule/amp/",
# "https://bustimings.in/msrtc/aurangabad-chandrapur/amp/",
# "https://bustimings.in/msrtc/chandrapur-aurangabad/amp/",
# "https://bustimings.in/msrtc/buldhana-aurangabad/amp/",


"https://bustimings.in/msrtc/aurangabad-buldhana/amp/",
"https://bustimings.in/msrtc/aurangabad-bhandara/amp/",
"https://bustimings.in/msrtc/bhandara-aurangabad/amp/",
"https://bustimings.in/msrtc/beed-aurangabad/amp/",
"https://bustimings.in/msrtc/aurangabad-beed/amp/",
"https://bustimings.in/msrtc/nanded-amravati-2/amp/",
"https://bustimings.in/msrtc/amravati-nanded/amp/",
"https://bustimings.in/msrtc/amravati-latur/amp/",
"https://bustimings.in/msrtc/latur-amravati/amp/",
"https://bustimings.in/msrtc/jalgaon-amravati/amp/",
"https://bustimings.in/msrtc/amravati-jalgaon/amp/",
"https://bustimings.in/msrtc/amravati-hingoli/amp/",
"https://bustimings.in/msrtc/hingoli-amravati/amp/",
"https://bustimings.in/msrtc/gondia-amravati/amp/",
"https://bustimings.in/msrtc/amravati-gondia/amp/",
"https://bustimings.in/msrtc/amravati-gadchiroli/amp/",
"https://bustimings.in/msrtc/gadchiroli-amravati/amp/",
"https://bustimings.in/msrtc/chandrapur-amravati/amp/",
"https://bustimings.in/msrtc/amravati-chandrapur/amp/",
"https://bustimings.in/msrtc/amravati-buldhana/amp/",
"https://bustimings.in/msrtc/buldhana-amravati/amp/",
"https://bustimings.in/msrtc/bhandara-amravati/amp/",
"https://bustimings.in/msrtc/amravati-bhandara/amp/",
"https://bustimings.in/msrtc/amravati-beed/amp/",
"https://bustimings.in/msrtc/beed-amravati/amp/",
"https://bustimings.in/msrtc/amravati-aurangabad/amp/",
"https://bustimings.in/msrtc/nagpur-amravati-2/amp/",
"https://bustimings.in/msrtc/nasik-amravati/amp/",
"https://bustimings.in/msrtc/amravati-nasik/amp/",
"https://bustimings.in/msrtc/amravati-parbhani/amp/",
"https://bustimings.in/msrtc/parbhani-amravati/amp/",
"https://bustimings.in/msrtc/pune-amravati/amp/",
"https://bustimings.in/msrtc/amravati-pune/amp/",
"https://bustimings.in/msrtc/shirdi-amravati/amp/",
"https://bustimings.in/msrtc/wardha-amravati/amp/",
"https://bustimings.in/msrtc/amravati-wardha/amp/",
"https://bustimings.in/msrtc/amravati-washim/amp/"

]

for i in range(76):
    r = requests.get(url[i])
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')
  
    print(soup.find_all('table'))
  