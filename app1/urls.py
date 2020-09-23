from django.urls import path

from app1 import views

urlpatterns = [
    path("computers/", views.ComputerAPIView.as_view()),
    path("computers/<str:pk>/", views.ComputerAPIView.as_view()),
]
