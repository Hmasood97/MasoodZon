from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.CharField(max_length=20)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    image = models.CharField(max_length=1000)
    price = models.IntegerField()
    def __str__(self):
        return self.title


class OrderBook(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.title