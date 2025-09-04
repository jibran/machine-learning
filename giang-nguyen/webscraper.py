import os
import re
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from bs4 import BeautifulSoup

disable_warnings(InsecureRequestWarning)

print("T431 * Machine learning 1 * Lab 1\nBy: Giang Nguyen\t#ID: 101593014\n\n")
# Example: https://edition.cnn.com/travel/hagia-sophia-istanbul-history-secrets

# Input with URL validation
url = ""
while not re.match("^https?://.*", url):
    url = input("Enter web URL: ")

# Scrape data
html = requests.get(url).text
document = BeautifulSoup(html, "html.parser")

# Refine content
for el in document.find_all("header") + document.find_all("script") + document.find_all("nav") + document.find_all("footer"):
    el.decompose()

text = str(document.text)
filecontent = "\n".join(line for line in text.splitlines() if line.strip())

# Store file
# Delete existing file before writing
filename = re.sub(r'[^a-zA-Z0-9\-\s]', "", document.title.string) + ".txt"
if filename == ".txt":
    filename = "extracted_document.txt"
if os.path.exists(filename):
    os.remove(filename)

with open(filename, "w", encoding="utf-8") as file:
    file.write(filecontent)
    file.flush()
    file.close()
    print("Saved content to file: ", filename)