from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=30)
    
    def __str__(self):
        return self.categoryName
    class Meta:
        verbose_name_plural = 'Categories'


class Listings(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length= 200)
    imageURL = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="user_watchlist")
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Listings'

class comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="comment")
    new_comment = models.CharField(max_length = 500)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, blank=True, null=True, related_name="listing")
    
    def __str__(self):
        return f"{self.author} comment on {self.listing}"
    class Meta:
        verbose_name_plural = 'Comments'
