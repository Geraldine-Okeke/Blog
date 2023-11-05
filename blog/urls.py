# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('full_post/<int:post_id>/', views.full_post, name='full_post'),
]
