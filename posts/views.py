from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def post_create(request):
  return HttpResponse("<h1>Crear post</h1>")

def post_detail(request):
  context = {
    "titulo": "Detalle"
  }
  return render(request, "index.html", context)

def post_list(request):
  queryset = Post.objects.all()
  context = {
    "titulo": "Listado",
    "objects_list":queryset
  }
  return render(request, "index.html", context)

def post_update(request):
  return HttpResponse("<h1>Actualizar posts</h1>")

def post_delete(request):
  return HttpResponse("<h1>Borrar posts</h1>")