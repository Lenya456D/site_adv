from django.urls import path
from advertisement import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    path('add_advertisement/', views.AddPage.as_view(), name='add_advertisement'),
    path('show_all/', views.ShowAllAdvert.as_view(), name='show_all'),
    path('search/', views.Search.as_view(), name='search'),
    path('<slug:advertisement_slug>/', views.PageView.as_view(), name='advertisement'),
]
