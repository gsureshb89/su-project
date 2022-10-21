from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from hero import views

urlpatterns = [
	path('heroes/', views.HeroList.as_view()),
	path('heroes/<int:pk>/', views.HeroDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)