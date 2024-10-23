from django.urls import path 

from . import views

urlpatterns = [
    path("dtl/", views.example_dtl, name="dtl"),
    path("test-dtl/", views.test_dtl, name="test-dtl"),
]