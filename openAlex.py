import requests

query = "cancer"
per_page = 5

url = f"https://api.openalex.org/works"
params = {
    "search": query,
    "per-page": per_page
}
headers = {
    "User-Agent": "codethecure@gmail.com"
}

response = requests.get(url, params=params, headers=headers)
papers = response.json()["results"]

for i, paper in enumerate(papers):
    title = paper.get("title", "No title")
    abstract = paper.get("abstract_inverted_index", None)
    doi = paper.get("doi", "No DOI")
    link = paper.get("primary_location", {}).get("landing_page_url", "No link")
    
    if abstract:
        word_positions = {pos: word for word, positions in abstract.items() for pos in positions}
        abstract_text = " ".join(word_positions[i] for i in sorted(word_positions))
    else:
        abstract_text = "No abstract"

    print(f"{i+1}. Title: {title}")
    print(f"DOI: {doi}")
    print(f"Link: {link}")
    print(f"Abstract: {abstract_text}")
    print("\n")