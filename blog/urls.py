from django.urls import path
from blog import views

urlpatterns = [
	path('', views.home, name='blog-home'),
	path('detail/<int:blog_id>/', views.detail, name='blog-detail'),
]