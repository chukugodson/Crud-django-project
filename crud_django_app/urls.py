from django.urls import path
from . import views

urlpatterns = [
	path('', views.register_view, name='register'),
	path ('comment', views.comment_view, name='comment'),
	path('logout', views.logout_view, name='logout-view'),
]