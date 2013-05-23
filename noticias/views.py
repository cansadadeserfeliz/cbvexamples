# -*- coding: utf-8 -*-

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.views.generic import JSONResponseMixin
from django.core.urlresolvers import reverse_lazy

from noticias.models import Noticia as NoticiasModel, Rubrica as RubricaModel
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



class NoticiasDeCine(ListView):
    model = NoticiasModel
    template_name = "noticias/cine_list.html"
    context_object_name = "noticias"

    def get_queryset(self):
        return super(NoticiasDeCine, self).get_queryset().filter(rubric__slug="cine")


class NoticiasPaginated(ListView):
    model = NoticiasModel
    template_name = "noticias/paginated_list.html"
    context_object_name = "noticias"
    paginate_by = 5


class Pubrica(DetailView):
    model = RubricaModel
    template_name = "noticias/rubrica.html"
    slug_field = "slug"

"""
class NoticiasJSON(JSONResponseMixin, ListView):
    model = NoticiasModel
    context_object_name = "noticias"
    template_name = "noticias/list.html"
"""