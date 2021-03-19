import json
from typing import Optional
import requests


class RedditAPIService:

    def __init__(self) -> None:
        from main import lru_cache
        self.lru_cache = lru_cache

    def get_response_reddit(self, q: Optional[str] = None) -> list:
        q = "News" if not q else q
        url = f'https://www.reddit.com/r/{q}/top/.json?limit=20'
        is_cache = self.lru_cache.cache.get(url)
        json_response = []
        if is_cache:
            return is_cache
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            response = json.loads(response.content.decode())
            articles = response.get('data', {}).get("children", {})
            json_response = [
                {
                    "headline": article.get("data", {}).get("title", ''),
                    "link": article.get("data", {}).get("url", ''),
                    "source": "reddit"
                } for article in articles]
        self.lru_cache.put(url, json_response or [])
        return json_response
