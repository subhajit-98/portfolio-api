from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_api.as_view(), name="blog_api"),
]