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
    hyperion.author = "Dan Simmons"
    hyperion.genre = "Sci-Fi"
    hyperion.image = "https://images-na.ssl-images-amazon.com/images/I/91cI7fKu0vL.jpg"
    hyperion.price = "$15"

    hill_House = Book()
    hill_House.title = "The Haunting of Hill House"
    hill_House.author = "Shirley Jackson"
    hill_House.genre = "Horror"
    hill_House.image = "https://images-na.ssl-images-amazon.com/images/I/91J6AQTt%2BGL.jpg"
    hill_House.price = "$20"

    pride_Prejudice = Book()
    pride_Prejudice.title = "Pride and Prejudice"
    pride_Prejudice.author = "Jane Austen"
    pride_Prejudice.genre = "Romance"
    pride_Prejudice.image = "https://cdn.shopify.com/s/files/1/0438/2233/products/Peacock_Cover_glitter_card_5_x_7.jpg?v=1571638712"
    pride_Prejudice.price = "$25"

    fahrenheit= Book()
    fahrenheit.title = "Fahrenheit 451"
    fahrenheit.author = "Ray Bradbury"
    fahrenheit.genre = "Sci-Fi"
    fahrenheit.image = "https://images-na.ssl-images-amazon.com/images/I/71OFqSRFDgL.jpg"
    fahrenheit.price = "$35"

    breath_Air = Book()
    breath_Air.title = "When Breath Becomes Air"
    breath_Air.author = "Paul Kalanithi"
    breath_Air.genre = "Biography"
    breath_Air.image = "https://images-na.ssl-images-amazon.com/images/I/717KRq4xxxL.jpg"
    breath_Air.price = "$15"
    
    lord_Rings = Book()
    lord_Rings.title = "The Lord Of The Rings"
    lord_Rings.author = "J.R.R Tolkein"
    lord_Rings.genre = "Fantasy"
    lord_Rings.image = "https://images-na.ssl-images-amazon.com/images/I/51tW-UJVfHL._SX321_BO1,204,203,200_.jpg"
    lord_Rings.price = "$15"
    
    books = [harry_Potter, steve_jobs, hyperion, hill_House, fahrenheit, breath_Air, lord_Rings ]
    

    return render(request, 'home-page.html', {'books': books})
