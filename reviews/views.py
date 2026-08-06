from django.shortcuts import render,redirect
from .models import Movie,Review

def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})

def review_list(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    reviews = movie.review_set.all()
    return render(request, "reviews.html", {
        "movie": movie,
        "reviews": reviews
    }) 

def add_review(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    if request.method == "POST":
        username = request.POST.get("username")
        rating = request.POST.get("rating")
        review = request.POST.get("review")

        Review.objects.create(
            movie=movie,
            username=username,
            rating=rating,
            review=review
        )

        return redirect("review_list", movie_id=movie_id)