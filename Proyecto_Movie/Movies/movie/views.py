from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

def home(request):


    return render(request, 'movie/templates/home.html')

class PeliculaListView(ListView):
    template_name = "movie/templates/movie_list.html"
    model = Pelicula


class PeliculaCreate(CreateView):
    template_name = "movie/templates/movie_create.html"
    model = Pelicula
    form_class = PeliculaForm
    success_url = reverse_lazy('movie_list')

class PeliculaDelete(DeleteView):
    template_name = "movie/templates/movie_delete.html"
    model = Pelicula
    success_url = reverse_lazy('movie_list')

class PeliculaUpdate(UpdateView):
    template_name = "movie/templates/movie_update.html"
    model = Pelicula
    form_class = PeliculaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('movie_update', args=[self.object.name]) + '?ok'
