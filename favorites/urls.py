from django.urls import path
from . import views

urlpatterns = [
    path("", views.favorites, name="Favorites"),
    path("movies/", views.favorite_movies, name="Favorite movies"),
    path("delete/", views.favorite_movies_delete, name="Favorite movies delete")
]