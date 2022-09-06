from django.urls import path, include
from .views import questionlist

urlpatterns = [
    path('api-auth/', questionlist.as_view()),
]