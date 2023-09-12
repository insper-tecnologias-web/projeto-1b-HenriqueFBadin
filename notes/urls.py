from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:index>', views.delete, name='index'),
    path('edit/<int:index>', views.edit, name='index'),
]
