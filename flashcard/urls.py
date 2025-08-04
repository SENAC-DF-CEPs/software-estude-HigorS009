from django.urls import path, include
from . import views

urlpatterns = [
  path('flashcard/', include('flashcard.urls')),
]