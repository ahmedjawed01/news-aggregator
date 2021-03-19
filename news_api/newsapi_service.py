from typing import Optional
from newsapi import NewsApiClient
from config import Config


class NewsAPIService:
    news_api = None
    lru_cache = None

    def __init__(self) -> None:
        from main import lru_cache
        self.lru_cache = lru_cache
        self.news_api = NewsApiClient(api_key=Config.API_KEY)

    def get_response(self, q: Optional[str] = None, scope: Optional[str] = None) -> list:
        response = []
        if not scope and not q:
            scope = "top"
            q = ''
        elif not q and scope:
            q = ''
            scope = "top"
        elif not scope and q:
            scope = "all"

        is_cache = self.lru_cache.cache.get(f"news_api_{scope}_{q}")
        if is_cache:
            return is_cache
        if scope == "all":
            response = self.get_everything(q)
        elif scope == "top":
            response = self.get_top_headlines(q)
        self.lru_cache.put(f"news_api_{scope}_{q}", response)
        return response

    def get_top_headlines(self, q: str) -> list:
        top_headlines = self.news_api.get_top_headlines(
            q=q,
            category="general",
            language='en',
        )
        return self.parse_response(top_headlines)

    def get_everything(self, q: str) -> list:
        everything = self.news_api.get_everything(
            q=q,
            language='en',
        )
        return self.parse_response(everything)

    def parse_response(self, response: dict) -> list:
        response_updated = []
        if response.get("status") == "ok":
            articles = response.get("articles")
            if articles:
                response_updated = [
                    {
                        "headline": article.get("title", ""),
                        "link": article.get("url", ""),
                        "source": "newsapi"}
                    for article in articles
                ]
        return response_updated
