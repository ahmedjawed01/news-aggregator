# News Aggregator

This is a repository for a web application developed with Python, FAST API, and REACT JS

### Features

1. **Aggregate Response of two different API** using [News API](https://newsapi.org/) and [Reddit](https://www.reddit.com/dev/api/)
2. **REST API** using [FAST API framework](https://github.com/tiangolo/fastapi)
3. **LRU Cache**
4. React JS
6. Custom Search

# Development

Following are instructions on setting up your development environment.

2. [Python](https://www.python.org/downloads/release/python-365/)

### Setting API's 

1. Install [virtualenv](https://pypi.org/project/virtualenv/) create and activate virtualenv
2. Clone this repo and `cd news_aggregator`
3. Run `pip3 install -r requirements.txt` to install the dependencies for this project.
4. Update .env file `NEWS_API_KEY` with your `NEWS API KEYS` and other things if required.
5. RUN `python3 main.py`

### Setting Frontend

1. Install [nodejs](https://nodejs.org/en/)
2. Change directory to `cd news_aggregator/react-news-app/`
3. Run `npm install`
4. Make sure to update src/config/index.js file with you running server url, by default it will be 0.0.0.0:8000
5. Run `npm start`
6. You can serve application [here](http://localhost:3000/) if everything is default.
7. You can search your queries in top search bar there.

### Run Test Cases
RUN `coverage run -m pytest tests/test.py`
RUN `coverage html`
Change directory to /htmlcov/ and open index.html you can see the coverage there.
