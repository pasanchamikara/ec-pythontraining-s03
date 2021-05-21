import requests
from bs4 import BeautifulSoup

url = ""
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all("div", {"class": ""})

for result in results:
    print(result.pretty())
    
# job_elems = results.find_all('section', class_='card-content')
# for job_elem in job_elems:
#     # Each job_elem is a new BeautifulSoup object.
#     # You can use the same methods on it as you did before.
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     print(title_elem.text)
#     print(company_elem.text)
#     print(location_elem.text)
