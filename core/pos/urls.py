from django.urls import path

from core.pos.views.citas.views import *

urlpatterns = [
    path('citas/', CitaListView.as_view(), name='cita_list'),
    path('citas/add/', CitaCreateView.as_view(), name='cita_create'),
    path('citas/update/<int:pk>/', CitaUpdateView.as_view(), name='cita_edit'),
    path('citas/delete/<int:pk>/', CitaDeleteView.as_view(), name='cita_delete'),
]


