from django.contrib.auth.views import LogoutView
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register')
]
