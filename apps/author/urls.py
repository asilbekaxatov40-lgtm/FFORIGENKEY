from django.urls import path
from .views import *

urlpatterns = [
    path('author/', AuthorListCreateView.as_view()),
    path('update/', AuthorUpdateView.as_view())
]