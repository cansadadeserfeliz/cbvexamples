# -*- coding: utf-8 -*-

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
)

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