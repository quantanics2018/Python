from bs4 import BeautifulSoup
import requests

url = "https://www.w3schools.com/js/default.asp"
response = requests.get(url)
if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    title = soup.title.text
    paragraphs = soup.find_all("p")
    
    print("Title:", title)
    print("Paragraphs:")
    for p in paragraphs:
        print(p.text)
