from typing import Optional

from fastapi.testclient import TestClient
from main import app

from reddit_api.reddit_service import RedditAPIService
from news_api.newsapi_service import NewsAPIService

client = TestClient(app)


def common_test_call(q: Optional[str] = None, scope: Optional[str] = None) -> None:
    news_api_service = NewsAPIService()
    reddit_api_service = RedditAPIService()

    news_api_service_response = news_api_service.get_response(q=q, scope=scope)
    reddit_api_service_response = reddit_api_service.get_response_reddit(q=q)
    print(news_api_service_response)
    response = client.get(f"/news?q={q}")

    assert isinstance(news_api_service_response, list)
    assert response.status_code == 200
    assert type(response.json()) == list
    for d in response.json():
        assert isinstance(d, dict)


def test_read_root():
    text = "Welcome to news aggregator"
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == f'"{text}"'


def test_news():
    reddit_service = RedditAPIService()
    service = NewsAPIService()
    expected = (service.get_response() + reddit_service.get_response_reddit(q=None))
    response = client.get("/news")

    assert response.status_code == 200
    assert type(response.json()) == list
    for d in response.json():
        assert type(d) == dict
    assert response.json() == expected


def test_news_with_q():
    q = 'bitcoin'
    scope = None

    news_api_service = NewsAPIService()
    reddit_api_service = RedditAPIService()

    news_api_service_response = news_api_service.get_response(q=q, scope=scope)
    reddit_api_service_response = reddit_api_service.get_response_reddit(q=q)

    expected = news_api_service_response + reddit_api_service_response

    response = client.get(f"/news?q={q}")

    assert response.status_code == 200
    assert type(response.json()) == list
    for d in response.json():
        assert isinstance(d, dict)
    assert response.json() == expected


def test_news_with_scope_top():
    q = None
    scope = 'top'
    common_test_call(q, scope)


def test_news_with_scope_all():
    q = None
    scope = 'all'
    common_test_call(q, scope)


def test_news_with_scope_all_and_q():
    q = "scope"
    scope = 'all'
    common_test_call(q, scope)


def test_news_with_scope_top_and_q():
    q = "top"
    scope = 'all'
    common_test_call(q, scope)


