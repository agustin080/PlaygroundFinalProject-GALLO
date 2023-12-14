from django.urls import path
from USUARIOS.views import registro, login_request, Logout, PerfilUsuarioCreateView, PerfilUsuarioUpdateView, perfil_usuario, acercademi, proposito, PerfilUsuarioListView

urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    path('crear_perfil/', PerfilUsuarioCreateView.as_view(), name='crear perfil'),
    path('<pk>/editar_perfil/', PerfilUsuarioUpdateView.as_view(), name='editar perfil'),
    path('perfil_usuario/', perfil_usuario, name='ver perfil'),
    path("acercademi/", acercademi, name = "acerca de mi"),
    path("proposito", proposito, name ="proposito"),
    path('lista/', PerfilUsuarioListView.as_view(), name='usuarios lista'),    
]