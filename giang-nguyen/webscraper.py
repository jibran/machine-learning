import os
import re
import sys

import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from bs4 import BeautifulSoup

disable_warnings(InsecureRequestWarning)

print("T431 * Machine learning 1 * Lab 1\nBy: Giang Nguyen\t#ID: 101593014\n\n")
# Example: https://jasoncmcbride.medium.com/how-to-create-a-life-you-love-0750e852475a
# Example: https://edition.cnn.com/travel/hagia-sophia-istanbul-history-secrets

# Input with URL validation
url = ""
while not re.match("^https?://.*", url):
    url = input("Enter web URL: ")

# Scrape data
try:
    html = requests.get(url).text
except Exception as e:
    print("Inaccessible or invalid URL\n", e)
    exit(1)
doc = BeautifulSoup(html, "html.parser", preserve_whitespace_tags=["div", "section", "p", "span"])
doc = BeautifulSoup(doc.prettify(), "html.parser")

# Refine content
for el in doc.find_all("header") + doc.find_all("script") + doc.find_all("nav") + doc.find_all("footer") + doc.find_all("nav"):
    el.decompose()

lines = doc.get_text(separator="\n", strip=True).splitlines()

if len(lines) <= 0:
    print("No content found")
    exit(1)

filecontent = "\n\r".join(lines)

# Store file
# Delete existing file before writing
filename = re.sub(r'[^a-zA-Z0-9()\',_\-\s]', "", doc.title.string.strip()) + ".txt"
if filename == ".txt":
    filename = "extracted_document.txt"
if len(filename) >= 150:
    filename = filename[:150] + ".txt"
if os.path.exists(filename):
    os.remove(filename)

with open(filename, "w", encoding="utf-8") as file:
    file.write(filecontent)
    file.flush()
    file.close()
    print("Saved content to file: ", filename)