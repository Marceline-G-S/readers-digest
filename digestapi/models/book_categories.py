# book_categories.py
from django.db import models
from django.contrib.auth.models import User

class Book_Categories(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
