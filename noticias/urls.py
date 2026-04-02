from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artigos),
    path('artigo/<int:id>/', views.detalhe_artigo),
    path('artigo/<int:id>/comentarios/', views.comentarios),
]