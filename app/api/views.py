from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from app.models.models import Movie, Review, Rating


def home(request):
    if not request.user.is_authenticated:
        return redirect("register")

    movies = Movie.objects.all().order_by("-release_year", "title")

    return render(
        request,
        "home.html",
        {"movies": movies}
    )

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    reviews = movie.reviews.select_related("user").all()
    ratings = movie.ratings.all()

    return render(
        request,
        "movie_detail.html",
        {
            "movie": movie,
            "reviews": reviews,
            "ratings": ratings,
        }
    )


def review_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    reviews = movie.reviews.select_related("user").all()

    user_reviewed = False

    if request.user.is_authenticated:
        user_reviewed = Review.objects.filter(
            movie=movie,
            user=request.user
        ).exists()

    return render(
        request,
        "reviews.html",
        {
            "movie": movie,
            "reviews": reviews,
            "user_reviewed": user_reviewed,
        }
    )


@login_required(login_url="login")
def add_review(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":

        rating_value = request.POST.get("rating")
        review_text = request.POST.get("review")

        if not rating_value or not review_text:
            messages.error(
                request,
                "Please provide both rating and review."
            )
            return redirect(
                "review_list",
                movie_id=movie_id
            )

        try:
            rating_value = int(rating_value)
        except ValueError:
            messages.error(
                request,
                "Invalid rating."
            )
            return redirect(
                "review_list",
                movie_id=movie_id
            )

        if rating_value < 1 or rating_value > 5:
            messages.error(
                request,
                "Rating must be between 1 and 5."
            )
            return redirect(
                "review_list",
                movie_id=movie_id
            )

        Review.objects.update_or_create(
            movie=movie,
            user=request.user,
            defaults={
                "review": review_text
            }
        )

        Rating.objects.update_or_create(
            movie=movie,
            user=request.user,
            defaults={
                "rating": rating_value
            }
        )

        messages.success(
            request,
            "Your review and rating have been saved!"
        )

    return redirect(
        "review_list",
        movie_id=movie_id
    )


def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get(
            "confirm_password"
        )

        if not username or not password:
            messages.error(
                request,
                "Username and password are required."
            )
            return redirect("register")

        if password != confirm_password:
            messages.error(
                request,
                "Passwords do not match."
            )
            return redirect("register")

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists."
            )
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Registration successful!"
        )

        return redirect("login")

    return render(
        request,
        "register.html"
    )


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

        messages.error(
            request,
            "Invalid username or password."
        )

        return redirect("login")

    return render(
        request,
        "login.html"
    )


def logout_view(request):

    logout(request)

    return redirect("register")