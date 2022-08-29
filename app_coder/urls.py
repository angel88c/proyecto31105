from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('curso/', curso),
    path('', inicio),
    path('cursos/', cursos, name='cursos'),
    path('estudiantes/', estudiantes),
    path('profesores/',profesores, name='profesores'),
    path('entregables/', entregables),
]
