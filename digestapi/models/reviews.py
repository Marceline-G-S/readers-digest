from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.CharField(max_length=400)
    date = models.DateField(auto_now_add=True)

