# -*- coding: utf-8 -*-

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
    FormView,
)
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy

from noticias.models import Noticia as NoticiasModel, Rubrica as RubricaModel
from noticias.forms  import NoticiaForm, ContactenosForm


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


class Contactenos(FormView):
    form_class = ContactenosForm
    template_name = "noticias/contactenos.html"
    success_url = reverse_lazy("gracias")


############################## Mixin #####################################
import json
from django.http import HttpResponse

class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    response_class = HttpResponse

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        response_kwargs['content_type'] = 'application/json'
        return self.response_class(
            self.convert_context_to_json(context),
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

