from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from publicaciones.models import publicacion
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class publicacionListView(LoginRequiredMixin, ListView):
    model = publicacion
    context_object_name = "publicaciones"
    template_name = "publicaciones/lista_publicaciones.html"
    login_url = "/usuarios/login"

class publicacionCreateView(LoginRequiredMixin, CreateView):
    model = publicacion
    template_name = "publicaciones/crear_publicacion.html"
    success_url = reverse_lazy('principal')
    fields = ['nombre_apellido', 'edad', 'titulo', 'autor', 'dificultad', "comentario", "imagen"]
    login_url = "/usuarios/login"

class publicacionUpdateView(LoginRequiredMixin, UpdateView):
    model = publicacion
    template_name = "publicaciones/editar_publicacion.html"
    success_url = reverse_lazy("publicaciones lista")
    fields = ['titulo', 'autor', 'dificultad', "comentario", "imagen"]
    login_url = "/usuarios/login"

class publicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = publicacion
    template_name = "publicaciones/eliminar_publicacion.html"
    success_url = reverse_lazy("publicaciones lista")
    login_url = "/usuarios/login"

class publicacionDetailView(LoginRequiredMixin, DetailView):
    model = publicacion
    template_name = "publicaciones/detalle_publicacion.html"
    success_url = reverse_lazy("publicaciones lista")
    login_url = "/usuarios/login"

def busqueda_en_bd(request):
    if request.GET.get("nombre", False):
        busqueda = request.GET["nombre"]
        lista_productos = publicacion.objects.filter(titulo__icontains=busqueda)
        return render(request, 'publicaciones/busqueda.html', {'lista': lista_productos})
    return render(request, 'publicaciones/busqueda.html')