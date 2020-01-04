from django.shortcuts import render
from django.http import HttpResponse
from . models import Book
# Create your views here.

def home(request):

    #Harry Potter Book
    harry_Potter = Book()
    harry_Potter.title = "Harry Potter"
    harry_Potter.author = "J.K Rowling"
    harry_Potter.genre = "Fantasy"
    harry_Potter.image = "https://wordery.com/jackets/0c0562f3/harry-potter-and-the-prisoner-of-azkaban-j-k-rowling-9781408855676.jpg"
    harry_Potter.price = "$25"

    steve_jobs = Book()
    steve_jobs.title = "Steve Jobs"
    steve_jobs.author = "Walter Isaacson"
    steve_jobs.genre = "Biography"
    steve_jobs.image = "https://images-na.ssl-images-amazon.com/images/I/81VStYnDGrL.jpg"
    steve_jobs.price = "$40"

    hyperion = Book()
    hyperion.title = "Hyperion"
    hyperion.genre = "Sci-Fi"
    hyperion.image = ""
    hyperion.price = "$15"
    

    return render(request, 'home-page.html', {'harry_potter': harry_potter})
