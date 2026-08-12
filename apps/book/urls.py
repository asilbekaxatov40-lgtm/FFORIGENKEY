from django.urls import path
from .views import *

urlpatterns = [
    path('book/', BookCreateListView.as_view()),
    path('update/', BookUpdateView.as_view())
]