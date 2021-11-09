from django.urls import path
from .views import movie_index,movie_delete,movie_detail,movie_create,movie_update
app_name="movie"

urlpatterns = [
    path('index/',movie_index,name="movie-index"),
    path('create',movie_create,name="movie-create"),
    path('<int:pk>/detail',movie_detail,name="movie-detail"),
    path('<int:pk>/update',movie_update,name="movie-update"),
    path('<int:pk>/delete',movie_delete,name="movie-delete"),
]