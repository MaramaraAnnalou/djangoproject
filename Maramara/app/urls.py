from django.urls import path
from app.views import HomePageView,AboutPageView

urlpatterns =[
    path('', HomePageView.as_view(), name='Home'),
    path('About/', AboutPageView.as_view(), name='About'),
]