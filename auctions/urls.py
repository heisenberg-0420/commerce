from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listings, name="create"),
    path("categories", views.view_categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("category/<str:title>", views.category, name="category"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("addWatchlist/<int:id>", views.add_watchlist, name="addWatchlist"),
    path("removeWatchlist/<int:id>", views.remove_watchlist, name="removeWatchlist"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("bid/<int:id>", views.bid, name="bid")
]
