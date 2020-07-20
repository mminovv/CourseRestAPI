from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/', views.CourseListView.as_view()),
    path('api/<int:pk>/', views.CourseDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)