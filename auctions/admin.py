from django.contrib import admin
from .models import User, Category, Listings, comments, Bids

# Register your models here.
admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Category)
admin.site.register(comments)
admin.site.register(Bids)