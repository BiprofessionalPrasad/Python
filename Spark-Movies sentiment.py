import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://www.msn.com/en-us?ocid=msedgntp&pc=W011&cvid=23f3c191f1c04ef881440f6710d1c727&ei=9'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract data (e.g., all paragraph texts)
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.get_text())
