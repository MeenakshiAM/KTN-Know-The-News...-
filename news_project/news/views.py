# news/views.py
from django.shortcuts import render
import requests

def index(request):
    articles = []
    if request.method == "POST":
        keyword = request.POST.get("keyword")
        if keyword:
            api_key = "give the api "  # Replace with your actual API key
            url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}"
            response = requests.get(url)
            data = response.json()
            articles = data.get("articles", [])
    return render(request, "news/index.html", {"articles": articles})
