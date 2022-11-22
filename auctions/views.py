from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listings, comments, Bids

all_categories = Category.objects.all()
active_listings = Listings.objects.filter(isActive=True)
return_register = "auctions/register.html"

def index(request):
    return render(request, "auctions/index.html", {
        "listings": active_listings
    })

def view_categories(request):
    return render(request, "auctions/categories.html", {
        "category": all_categories
    })

def bid(request, id):
    return
    
def comment(request, id):
    current_user= request.user
    listing_item = Listings.objects.get(pk = id)
    new_comment= request.POST["comment"]
    save_comment = comments(
        author = current_user,
        listing = listing_item,
        new_comment = new_comment
    )
    save_comment.save()
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def category(request, title):
    category = Category.objects.get(categoryName = title)
    selected_category = Listings.objects.filter(isActive=True, category=category)
    return render(request, "auctions/category.html",{
        "active_listings": selected_category
    })
    
def listing(request, id):
    listing_item = Listings.objects.get(pk = id)
    all_comments = comments.objects.filter(listing = listing_item)
    listing_in_watchlist = request.user in listing_item.watchlist.all()
    return render(request, "auctions/listing.html", {
        "listing_item": listing_item,
        "listing_in_watchlist": listing_in_watchlist,
        "all_comments": all_comments
    })
    
def remove_watchlist(request, id):
    listing_item = Listings.objects.get(pk = id)
    current_user= request.user
    listing_item.watchlist.remove(current_user)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def add_watchlist(request, id):
    listing_item = Listings.objects.get(pk = id)
    current_user= request.user
    listing_item.watchlist.add(current_user)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def watchlist(request):
    current_user= request.user
    listings = current_user.user_watchlist.all()
    return render(request, "auctions/watchlist.html",{
        "listings": listings
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, return_register, {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, return_register, {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, return_register)
    
def create_listings(request):
    if request.method == "GET":
        return render(request, "auctions/create.html", {
            "categories": all_categories
        })
    else:
        title = request.POST["title"]
        description = request.POST["description"]
        image_url = request.POST["imageURL"]
        price = request.POST["price"]
        category = request.POST["category"]
        current_user = request.user
        category_data = Category.objects.get(categoryName = category)
        new_listing = Listings(
            title = title,
            description = description,
            imageURL = image_url,
            price = float(price),
            owner = current_user,
            category = category_data
        )
        new_listing.save()
        return HttpResponseRedirect(reverse("index"))
