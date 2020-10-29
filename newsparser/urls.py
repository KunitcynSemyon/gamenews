from . import views
from django.urls import path, include

app_name = 'newsparser'

urlpatterns = [
	path('stopgame/', views.index),
]