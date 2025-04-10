from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('memorials/<int:id>/', views.memorial_detail, name='memorial-detail'),

]