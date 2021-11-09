from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def movie_index(request):
    all_movies = Movie.objects.all()
    print("all Movies--->", all_movies)
    return render(request, 'movie/movie_index.html', context={'movies': all_movies})


# @csrf_exempt
# def movie_create(request):
#     if request.method == 'POST':
#         print(request.POST)
#         movie_name=request.POST.get('name')
#         movie_desc=request.POST.get('desc')
#         movie_likes=request.POST.get('likes')
#         # movie_data={'name':movie_name,'description':movie_desc,'likes':movie_likes}
#         movie_object=Movie.objects.create(name=movie_name,description=movie_desc,likes=movie_likes,active=True)
#
#
#     # all_movies=Movie.objects.all()
#
#         print(movie_object)
#         return redirect('movie:movie-index')
#     return render(request,'movie/movie_create.html')


def movie_create(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST,files=request.FILES)
        if form.is_valid():
            print("Yes it's valid")

            form.save()
            return redirect('movie:movie-index')
    return render(request, 'movie/movie_create.html', {'form': form})


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    print(movie.review_set.all())
    return render(request, 'movie/movie_detail.html', context={'movie': movie})


def movie_delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect('movie:movie-index')


def movie_update(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)
    if request.method == "POST":
        form = MovieForm(data=request.POST, files=request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:movie-detail', pk=movie.id)

    return render(request, 'movie/movie_update.html', {'form': form, 'movie': movie})
