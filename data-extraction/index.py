import requests
from bs4 import BeautifulSoup

# Get https://catalog.data.gov/dataset website
page = requests.get('https://catalog.data.gov/dataset')

# Print page contents
#print page.status_code
#print page.headers
#print page.encoding
#page.text

# Parse page text to HTML
# soup = BeautifulSoup(page.text, 'html5lib')
soup = BeautifulSoup(page.text, 'lxml')

# Get all h3 elements with class 'dataset-heading'
h3s = soup.find_all('h3', {'class' : 'dataset-heading'})

# Print h3 elements line by line
for h3 in h3s:
    print "\n"
    page = requests.get("https://catalog.data.gov" + h3.find('a')["href"])
    print page.text
    print "\n"