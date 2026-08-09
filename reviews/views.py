from django.shortcuts import render, redirect
from .models import Movie, Review, Rating
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})


def review_list(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    reviews = movie.review_set.all()

    user_reviewed = False

    if request.user.is_authenticated:
        user_reviewed = Review.objects.filter(
            movie=movie,
            user=request.user
        ).exists()

    return render(request, "reviews.html", {
        "movie": movie,
        "reviews": reviews,
        "user_reviewed": user_reviewed
    })


def add_review(request, movie_id):
    if not request.user.is_authenticated:
        return redirect("login")

    movie = Movie.objects.get(id=movie_id)

    if request.method == "POST":
        rating = request.POST.get("rating")
        review = request.POST.get("review")

        Review.objects.create(
            movie=movie,
            user=request.user,
            review=review
        )

        Rating.objects.create(
            movie=movie,
            user=request.user,
            rating=rating
        )

        return redirect("review_list", movie_id=movie_id)

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


def logout_view(request):
    logout(request)
    return redirect("login")