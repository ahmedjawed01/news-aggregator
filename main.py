from typing import Optional
import uvicorn
from fastapi import FastAPI
from news_api.newsapi_service import NewsAPIService
from reddit_api.reddit_service import RedditAPIService
from cache import LRUCache
from config import Config
from fastapi.middleware.cors import CORSMiddleware


# FAST API app
app = FastAPI()

# Initializing LRUCache object
lru_cache = LRUCache(Config.CAPACITY)

# Allowed Origin
origins = Config.ALLOWED_HOST

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["get"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> str:
    return "Welcome to news aggregator"


@app.get("/news")
def news(q: Optional[str] = None, scope: Optional[str] = None) -> list:
    response = []
    response.extend(NewsAPIService().get_response(q=q, scope=scope))
    response.extend(RedditAPIService().get_response_reddit(q))
    return response


if __name__ == '__main__':
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)
