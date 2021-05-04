from django.urls import path

from django_books import views

urlpatterns = [
    path('author/', views.AuthorListView.as_view()),
    path('author/<int:pk>/', views.AuthorDetailView.as_view()),
]
