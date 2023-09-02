from bs4 import BeautifulSoup
import requests

# URL of the webpage
url = "https://www.w3schools.com/js/default.asp"

# Send an HTTP request and get the HTML content
response = requests.get(url)
if response.status_code == 200:
    html_content = response.content
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Find all image tags and extract their source URLs
    img_tags = soup.find_all("img")
    for img_tag in img_tags:
        img_src = img_tag.get("src")
        print("Image Source:", img_src)
else:
    print("Failed to retrieve the webpage.")
