from django.urls import path,include
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
    path('studentapi/', views.studentapi, name = 'student-api'),
    path('', views.apiall, name = 'api'),
]
