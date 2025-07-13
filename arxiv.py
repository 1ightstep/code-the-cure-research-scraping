import requests
import xml.etree.ElementTree as ET

query = "cancer"
maxResults = 2000
url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={str(maxResults)}"

response = requests.get(url)
root = ET.fromstring(response.content)

ns = {
    'atom': 'http://www.w3.org/2005/Atom',
    'arxiv': 'http://arxiv.org/schemas/atom'
}

for index, entry in enumerate(root.findall('atom:entry', ns)):
    title = entry.find('atom:title', ns).text.strip()
    summary = entry.find('atom:summary', ns).text.strip()
    link = entry.find('atom:id', ns).text.strip()

    doi_element = entry.find('arxiv:doi', ns)
    doi = doi_element.text.strip() if doi_element is not None else "DOI not available"

    print(f"{index + 1}Title: {title}\nLink: {link}\nDOI: {doi}\nSummary: {summary}\n\n")
