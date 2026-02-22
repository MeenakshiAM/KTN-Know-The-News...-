from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def index(request):
    articles = []
    error = None

    if request.method == "POST":
        keyword = request.POST.get("keyword")

        if keyword:
            api_key = os.getenv("NEWS_API_KEY")

            # Handle missing API key
            if not api_key:
                error = "API key not configured. Please set NEWS_API_KEY in .env file."
            else:
                url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}"
                response = requests.get(url)
                data = response.json()
                articles = data.get("articles", [])

    return render(request, "news/index.html", {
        "articles": articles,
        "error": error
    })