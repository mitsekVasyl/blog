""" URL patterns for users """

from django.urls import include, path

from . import views

app_name = 'users'
urlpatterns = [
	# Auth url for default
	path('', include('django.contrib.auth.urls')),
	# Registration
	path('register/', views.register, name='register'),
]