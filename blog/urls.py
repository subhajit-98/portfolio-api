from django.urls import path
from blog import views

urlpatterns = [
    path('<int:page_no>/', views.blog_api.as_view(), name="blog_api"),
]