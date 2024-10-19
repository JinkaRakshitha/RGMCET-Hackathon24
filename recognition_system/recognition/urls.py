from django.urls import path
from . import views

urlpatterns = [
    path('rankings/', views.display_rankings, name='rankings'),
]

