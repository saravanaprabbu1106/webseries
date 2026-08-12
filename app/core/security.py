from django.contrib.auth.decorators import login_required


def authenticated(view):
    return login_required(view)