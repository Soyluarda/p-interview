# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from bs4 import BeautifulSoup
from models import posts
import requests



def refresh():
    post_list = posts.objects.all()
    url = 'https://blog.prisync.com/feed/'
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'xml')
    soups = soup.find_all('item')
    same_list = []
    for i in post_list:
        same_list.append(i.title)
    for i in soups:
        if i.title.text not in same_list:
            create_post = posts(title=i.title.text,link=i.link.next,category=i.category.text,creator=i.creator.text,pubdate=i.pubDate.text[:16],description=i.description.text)
            create_post.save()

def index(request):
    post_list = posts.objects.all()
    all_posts = []
    if request.method == 'POST':
        refresh()
    for i in post_list:
        dicty = {
            'title': i.title,
            'category': i.category,
            'link': i.link,
            'creator': i.creator,
            'pubdate': i.pubdate,
            'description': i.description,
        }
        all_posts.append(dicty)

    return render(request,'index.html',{'post_list':all_posts})