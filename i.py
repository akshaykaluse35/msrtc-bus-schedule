import requests
from bs4 import BeautifulSoup

url = 'https://bustimings.in/msrtc/shirdi-nasik/amp/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tbl = soup.find('table')

for time in tbl.find_all('tbody'):
    rows = time.find_all('tr')
    for row in rows:
        pl_teams = row.find('td').text
        pl_points = row.find('td').text
        print(pl_teams, pl_points)
