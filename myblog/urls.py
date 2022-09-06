from django.urls import path, include
from .views import questionlist

urlpatterns = [
    path('questions/', questionlist.as_view()),
]