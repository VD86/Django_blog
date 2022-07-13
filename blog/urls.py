from blog.views import ListObjectsView, DetailObjectsView, SearchResultsView
from django.urls import path

urlpatterns = [
    path('', ListObjectsView.as_view()),
    path('<int:pk>', DetailObjectsView.as_view(), name='detail'),
    path('search/', SearchResultsView.as_view(), name="search_results"),
]
