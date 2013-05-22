# -*- coding: utf-8 -*-

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.core.urlresolvers import reverse_lazy

from noticias.models import Noticia as NoticiasModel
from noticias.forms  import NoticiaForm

class Noticias(ListView):
    model = NoticiasModel
    template_name = "noticias/list.html"
    context_object_name = "noticias"

class Noticia(DetailView):
    model = NoticiasModel
    template_name = "noticias/detail.html"
    context_object_name = "noticia"

class UpdateNoticia(UpdateView):
    model = NoticiasModel
    template_name = "noticias/form.html"
    form_class = NoticiaForm
    success_url = reverse_lazy("noticias")

class CreateNoticia(CreateView):
    model = NoticiasModel
    template_name = "noticias/form.html"
    form_class = NoticiaForm
    success_url = reverse_lazy("noticias")

class DeleteNoticia(DeleteView):
    model = NoticiasModel
    success_url = reverse_lazy("noticias")
    template_name = "noticias/delete_confirm.html"