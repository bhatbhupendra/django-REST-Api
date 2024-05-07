from django.urls import path,include
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(),name="vlogpost-view-create"),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestory.as_view(),name="update"),
]
