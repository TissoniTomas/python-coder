from django.urls import path
from .views import (
    about_view, blog_list_view, blog_detail_view,
    signup_view, profile_view, mensaje_view, mensajes_list_view
)

urlpatterns = [
    path('about/', about_view, name='about'),
    path('pages/', blog_list_view, name='blog_list'),
    path('pages/<int:pageId>/', blog_detail_view, name='blog_detail'),
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/profile/', profile_view, name='profile'),
    path('messages/', mensajes_list_view, name='mensajes'),
    path('messages/new/', mensaje_view, name='nuevo_mensaje'),
]
