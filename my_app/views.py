from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from bs4 import BeautifulSoup
from django.urls import reverse
from requests.compat import quote_plus
from . import models
from .models import Search


import requests

# Create your views here.


def home(request):
    return render(request, 'base.html')
def new_search(request):


    front=[]

    search=request.POST.get('search')

    if search!=None:
        x=models.Search.objects.create(search=search)
    else:
        pass
    context={'a':Search.objects.all()[::-1]}



        #return HttpResponseRedirect(reverse('new_search'))





    return render(request,'my_apps/new_search.html', context)
# return HttpResponseRedirect(reverse('myforum.views.topic', args=[topic_id]))

def delete(request,pk1):
    dele=get_object_or_404(Search, pk=pk1)

    print(dele.id)

    dele.delete()




   # return HttpResponse("del %s"%pk1)

    return HttpResponseRedirect(reverse('new_search'))


def clearall(request):
    Search.objects.all().delete()

    return HttpResponseRedirect(reverse('home'))



