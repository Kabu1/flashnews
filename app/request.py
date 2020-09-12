from app import app
import urllib.request,json
from .models import article
Article = article.Article


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]