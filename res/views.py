from django.shortcuts import render
import requests
from django.http import HttpResponse ,JsonResponse
# Create your views here.

def index(request):
    k=request.GET.get('name')
    kl=[]
    t={}
    print(k)
    url = 'https://vartapratikriya-api.vercel.app/articles/headlines'
    response = requests.get(url)
    news = response.json()
    articles = news['articles']
    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles = articles[i]
        o=myarticles['source']['name'].replace(" ", "")
        if(o.lower()==k.lower()):
            # print(myarticles)
            t=myarticles
            kl.append(t)
            print(kl)
    # return render(request, 'index.html', context = {"mylist":mylist})
    return JsonResponse(kl,safe=False)