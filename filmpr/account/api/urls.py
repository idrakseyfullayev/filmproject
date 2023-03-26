from django.urls import path
from account.api import views

app_name = 'account'

urlpatterns = [
    path("users/", views.UserListAPIView.as_view(), name="users"),
    path("user-create/", views.UserCreateAPIView.as_view(), name="user-create"),
    path('user-update/<int:id>/', views.UserUpdateAPIView.as_view(), name="user-update"),
    path('user-destroy/<int:id>/', views.UserDestroyAPIView.as_view(), name="user-destroy"),
    path("accounts/", views.AccountListAPIView.as_view(), name="accounts"),
    path("account-create/", views.AccountCreateAPIView.as_view(), name="account-create"),
    path('account-update/<int:id>/', views.AccountUpdateAPIView.as_view(), name="account-update"),
    path('account-destroy/<int:id>/', views.AccountDestroyAPIView.as_view(), name="account-destroy"),

]