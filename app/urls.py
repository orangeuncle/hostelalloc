
from django.urls import path
from . import views        # Imports view. Views carries the page views

urlpatterns = [
    # path('', views.home.as_view(), name='Homepage'),      # Points to the Home function in Views as home
    path('', views.home, name='Homepage'),      # Points to the Home function in Views as home
    path('about/', views.about, name='about'),      # Points to about function as about
    path('search/', views.search, name='search'),
    path('playground', views.playground, name='playground'),
]