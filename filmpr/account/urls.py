from django.urls import path, include
from account import views

app_name = 'account'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginUserView.as_view(), name="login"),
    path("logout/", views.LogoutUserView.as_view(), name="logout"),
    path("loginpage/", views.LoginPageView.as_view(), name="loginpage"),
]
