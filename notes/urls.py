from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:index>', views.delete, name='delete'),
    path('edit/<int:index>', views.edit, name='edit'),
    path('tags', views.tags, name='tags'),
    path('note-list/<int:index>', views.note_list, name='note-list'),
]
