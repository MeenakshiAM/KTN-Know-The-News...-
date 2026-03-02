from django.shortcuts import render
import requests
import xml.etree.ElementTree as ET
from django.conf import settings


def home(request):
    # Fetch trending news (reuse TOI RSS)
    articles = fetch_toi_news()[:6]  # limit to 6 for homepage

    return render(request, "news/home.html", {
        "articles": articles
    })

def fetch_toi_news():
    url = "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        
        articles = []
        for item in root.findall(".//item"):
            title = item.find("title").text if item.find("title") is not None else "No Title"
            description = item.find("description").text if item.find("description") is not None else ""
            link = item.find("link").text if item.find("link") is not None else "#"
                        
            articles.append({
                "title": title,
                "description": description,
                "url": link
            })
        return articles
    except Exception as e:
        print(f"Error fetching TOI news: {e}")
        return []

def index(request):
    articles = []
    error = None

    if request.method == "POST":
        keyword = request.POST.get("keyword")
        print("KEYWORD:", keyword)   

        if keyword:
            api_key = settings.NEWS_API_KEY
            print("API KEY:", api_key) 

            # Handle missing API key
            if not api_key:
                error = "API key not configured. Please set NEWS_API_KEY in .env file."
            else:
                url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}"
                response = requests.get(url)
                data = response.json()
                print(data)
                articles = data.get("articles", [])
                
    return render(request, "news/index.html", {
        "articles": articles,
        "error": error
    })

def india_news(request):
    articles = fetch_toi_news()
    return render(request, "news/india.html", {
        "articles": articles
    })