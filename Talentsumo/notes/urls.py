from django.urls import path
from notes import views

urlpatterns = [
    path('notes/', views.note_list, name='note-list'),
    path('notes/<int:note_id>/', views.note_detail, name='note-detail'),
]
