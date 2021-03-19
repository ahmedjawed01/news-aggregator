from decouple import config


class Config:
    API_KEY = config('NEWS_API_KEY')
    CAPACITY = config('LRU_CACHE_CAPACITY')
    HOST = str(config('HOST', '0.0.0.0'))
    PORT = int(config('PORT', 8000))
    ALLOWED_HOST = str(config('ALLOWED_HOST', ["http://localhost:3000"]))
