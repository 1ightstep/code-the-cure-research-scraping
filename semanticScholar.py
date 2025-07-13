import requests

url = "https://api.semanticscholar.org/graph/v1/paper/search"
params = {
    "query": "cancer",
    "fields": "title,abstract,url",
    "limit": 5
}

res = requests.get(url, params=params)
papers = res.json()["data"]
print(papers)

for paper in papers:
    print(f"Title: {paper['title']}")
    print(f"DOI: {paper.get('doi', 'N/A')}")
    print(f"Link: {paper['url']}")
    print(f"Abstract: {paper.get('abstract', 'No abstract')}")
    print("\n")
