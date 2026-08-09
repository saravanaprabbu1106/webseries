from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("register/", views.register, name="register_page"),
    path("login/", views.login_view, name="login"),
    path("home/", views.home, name="home"),
    path("reviews/<int:movie_id>/", views.review_list, name="review_list"),
    path("reviews/<int:movie_id>/add/", views.add_review, name="add_review"),
    path("logout/", views.logout_view, name="logout"),
]