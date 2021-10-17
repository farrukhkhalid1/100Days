import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla"


def get_news():
    news_parameters = {
        "apiKey": "new your key",
        "q": COMPANY_NAME,
        "sortBy": "popularity",
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()

    news = news_response.json()
    top_news = news["articles"][:4]

    for news in top_news:
        top_news_title = news["title"]
        top_news_description = news["description"]
        print(f"Title: {top_news_title}\nDescription: {top_news_description}")


stock_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": "new your key",
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()

stock_data = stock_response.json()
closing_stock = float(stock_data["Time Series (60min)"]["2021-10-15 20:00:00"]["4. close"])
opening_stock = float(stock_data["Time Series (60min)"]["2021-10-14 20:00:00"]["4. close"])

change = (closing_stock - opening_stock) / closing_stock * 100

if -5 >= change or change >= 5:
    get_news()
