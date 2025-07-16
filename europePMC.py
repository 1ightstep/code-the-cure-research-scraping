import requests

query = "cancer"
page_size = 10
format = "json"

url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

params = {
    "query": query,
    "format": format,
    "pageSize": page_size
}

response = requests.get(url, params=params)
data = response.json()

results = data.get("resultList", {}).get("result", [])

for index, paper in enumerate(results):
    print(paper)
    title = paper.get("title", "No title")
    abstract = paper.get("abstractText", "No abstract")
    doi = paper.get("doi", "No DOI")
    source = paper.get("source", "Unknown")
    pmid = paper.get("id", "No ID")

    # Try to create a link
    if source == "MED":
        link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    elif source == "PMC":
        link = f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmid}/"
    else:
        link = f"https://doi.org/{doi}" if doi != "No DOI" else "No link available"

    print(f"{index + 1}. Title: {title}")
    print(f"Abstract: {abstract}")
    print(f"DOI: {doi}")
    print(f"Link: {link}")
    print("\n")
