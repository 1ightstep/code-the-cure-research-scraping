import requests
from xml.etree import ElementTree as ET

EMAIL = "your_email@example.com"
TOOL = "MyResearchApp"

search_query = "cancer"
retmax = 5
search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
search_params = {
    "db": "pubmed",
    "term": search_query,
    "retmax": retmax,
    "retmode": "xml",
    "tool": TOOL,
    "email": EMAIL
}

search_response = requests.get(search_url, params=search_params)
search_root = ET.fromstring(search_response.content)
id_list = [id_elem.text for id_elem in search_root.findall(".//Id")]

fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
fetch_params = {
    "db": "pubmed",
    "id": ",".join(id_list),
    "retmode": "xml",
    "tool": TOOL,
    "email": EMAIL
}

fetch_response = requests.get(fetch_url, params=fetch_params)
fetch_root = ET.fromstring(fetch_response.content)

articles = fetch_root.findall(".//PubmedArticle")

for i, article in enumerate(articles):
    title = article.findtext(".//ArticleTitle", "No title")
    abstract_elem = article.find(".//Abstract/AbstractText")
    abstract = abstract_elem.text if abstract_elem is not None else "No abstract"
    
    pmid = article.findtext(".//PMID", "No PMID")
    doi = "No DOI"
    
    for id_elem in article.findall(".//ArticleId"):
        if id_elem.attrib.get("IdType") == "doi":
            doi = id_elem.text
            break

    link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"

    print(f"{i+1}. Title: {title}")
    print(f"PMID: {pmid}")
    print(f"DOI: {doi}")
    print(f"Link: {link}")
    print(f"Abstract: {abstract}")
    print("\n")

