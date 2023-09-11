from django.urls import path
from .views import MyLoginView, SignUpView
from django.contrib.auth.views import LogoutView





urlpatterns = [
        path('login/', MyLoginView.as_view(),name='login'),
        path('logout/', LogoutView.as_view(next_page='index'),name='logout'),
        path('register/', SignUpView.as_view(), name='register'),
]