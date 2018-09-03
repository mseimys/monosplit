from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .utils import get_admin


def index(request):
    return render(request, 'index.html', {
        'instance': settings.INSTANCE_NAME,
        'logged_in': request.user.is_authenticated,
        'user': request.user,
    })

def login_view(request):
    login(request, get_admin())
    return redirect(reverse('dashboard:index'))

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('dashboard:index'))
