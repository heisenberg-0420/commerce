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
    path("category/<str:title>", views.category, name="category")
]
