from django.db import models
from django.conf import settings

# Create your models here.

category_Choices = (
    ('Fa', 'Fantasy'),
    ('Bi', 'Biographies'),
    ('Sc', 'Sci-Fi'),
    ('Ho', 'Horror'),
    ('Ro', 'Romance')
)


#book Class
class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=250)
    genre = models.CharField(choices = category_Choices, max_length=250)
    image = models.CharField(max_length=1000)
    price =models.CharField(max_length=250)
    def __str__(self):
        return self.title



#inidivdual book order. Basically once you add it into the thang
class OrderBook(models.Model):
    item = models.ForeignKey(Book, on_delete = models.CASCADE )

    def __str__(self):
        return self.title


#order class is essentially the shopping cart
class Order (models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderBook)
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return self.title