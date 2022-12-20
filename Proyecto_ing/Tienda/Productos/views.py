from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

def home(request):

    return render(request, 'Productos/templates/home.html')


class ProductoListView(ListView):
    template_name = 'Productos/templates/producto_list.html'
    model = Productos

class ProductoCreate(CreateView):
    template_name = 'Productos/templates/producto_create.html'
    model = Productos
    form_class = ProductoForm
    success_url = reverse_lazy('producto_list')

class ProductoDelete(DeleteView):
    template_name = 'Productos/templates/producto_delete.html'
    model = Productos
    success_url = reverse_lazy('producto_list')

class ProductoUpdate(UpdateView):
    template_name = 'Productos/templates/producto_update.html'
    model = Productos
    form_class = ProductoForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('producto_update', args=[self.object.id]) + '?ok'

