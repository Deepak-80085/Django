from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound

from .util import list_entries, get_entry, save_entry, markdown_to_html
import random

def index(req):
    return render(req, "encyclopedia/index.html", {
        "entries": list_entries()
    })

def entry(req,title):
    content = get_entry(title)
    if title is None:
        return HttpResponseNotFound("Page not found")
    else:
        return render(req,"encyclopedia/entry.html",{
            "title":title,
            "content": markdown_to_html(content)
        })

def new_entry(req):
    if req.method == 'POST':
        title = req.POST['title']
        content = req.POST['content']

        if get_entry(title) is not None:
            return render(req,'encyclopedia/new_entry.html',{'error':'Title already exists'})

        save_entry(title,content)
        return redirect('entry',title=title)

    return render(req,'encyclopedia/new_entry.html')

def edit_entry(req,title):
    content = get_entry(title)
    if content is None:
        return HttpResponseNotFound("Page not found")
    if req.method == 'POST':
        new_content = req.POST['content']
        save_entry(title,new_content)
        return redirect('entry',title=title)

    return render(req,'encyclopedia/edit_entry.html',{'title':title,'content':content})

def search(req):
    query = req.GET.get('q','')
    entries = list_entries()
    results = []
    for entry in entries:
        if query.lower() in entry.lower():
            results.append(entry)

    return render(req,'encyclopedia/search.html',{'query':query,'entries':results})

def random_entry(req):
    entry = list_entries()
    title = random.choice(entry)
    return redirect('entry',title=title)