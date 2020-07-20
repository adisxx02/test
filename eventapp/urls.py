from django.urls import path
from . import views

urlpatterns = [
    path('acara', views.Acara.as_view(), name='acara'),
    path('bagian/<int:id>', views.Bagian.as_view(), name='bagian'),
    path('tugas/<int:id>', views.Tugas.as_view(), name='tugas'),
    path('edit-tugas/<int:id>', views.EditTugas.as_view(), name='edit-tugas'),
    path('print-acara', views.PrintAcara.as_view(), name='print-acara'),
]