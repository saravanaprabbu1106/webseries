from django.shortcuts import render, redirect
from .models import Movie, Review
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


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


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration successful!")
        return redirect("login")

    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")    