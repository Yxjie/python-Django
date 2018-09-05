from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import *


# Create your views here.
# HttpRequest
def index(request):
    # HttpResponse
    return HttpResponse('<h1>Hello Django !!!<h1>')


def load_html(request):
    list = ['Kotlin', 'Java', 'Python']
    books = BookInfo.objects.all()

    context = {'list': list, 'booklist': books}
    return render(request, 'booktest/index.html', context)


def detail(request, id):
    book = BookInfo.objects.get(id=id)
    list = book.heroinfo_set.all()
    context = {'herolist': list}
    return render(request, 'booktest/detail.html', context)
