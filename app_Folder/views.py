from django.shortcuts import render
from django.http import HttpResponse
from . models import Book
# Create your views here.

def home(request):

    harry_potter = Book()

    return render(request, 'home-page.html', {'harry_potter': harry_potter})
