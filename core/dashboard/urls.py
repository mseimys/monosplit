from django.urls import path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view),
    path('logout', views.logout_view),
]
