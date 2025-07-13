import requests
import xml.etree.ElementTree as ET

query = "cancer"
maxResults = 2000
url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={str(maxResults)}"

response = requests.get(url)
root = ET.fromstring(response.content)

for index, entry in enumerate(root.findall("{http://www.w3.org/2005/Atom}entry")):
    title = entry.find("{http://www.w3.org/2005/Atom}title").text
    summary = entry.find("{http://www.w3.org/2005/Atom}summary").text
    print(f"{index + 1}\nTitle: {title}\nSummary: {summary}")