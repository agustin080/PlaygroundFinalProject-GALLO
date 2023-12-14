from django.urls import path
from publicaciones.views import publicacionListView, publicacionCreateView, publicacionDeleteView, publicacionUpdateView, publicacionDetailView
from publicaciones.views import busqueda_en_bd

urlpatterns = [
    path('lista/', publicacionListView.as_view(), name='publicaciones lista'),
    path('crear/', publicacionCreateView.as_view(), name='publicaciones crear'),
    # En estas vistas necesitamos agregar un detalle extra que es el argumento <pk>
    # con este argumento que traemos desde el html se identifica cuál es la venta que vamos a acceder.
    path('<pk>/eliminar/', publicacionDeleteView.as_view(), name='publicaciones eliminar'),
    path('<pk>/editar/', publicacionUpdateView.as_view(), name='publicaciones editar'),
    path('<pk>/detalle/', publicacionDetailView.as_view(), name='publicaciones detalle'),
    path('busqueda_bd/', busqueda_en_bd, name='busqueda en bd'),
]