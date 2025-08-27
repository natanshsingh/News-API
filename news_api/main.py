import requests

query = input("What do you want to see news about?")

api = "6134df659e6e40b8a9a305bf01641774"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-18&sortBy=publishedAt&apiKey=6134df659e6e40b8a9a305bf01641774"

print(url)

r = requests.get(url)
data = r.json()

articles = data["articles"]

for article in articles:
    print(f"Title: {article['title']},\n{article['url']}")
    print("\n************************************\n")