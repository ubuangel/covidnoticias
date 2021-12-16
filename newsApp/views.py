from django.shortcuts import render
from newsapi import NewsApiClient
#from newsapi.newsapi_client import NewsApiClient
# Create your views here.


def index(request):
    newsApi = NewsApiClient(api_key='f7fcfea42d634e00b81d4dd87f459c26')
    headLines = newsApi.get_top_headlines(sources='abc-news,infobae')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, "main/index.html", context={"mylist": mylist})
