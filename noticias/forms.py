# -*- coding: utf-8 -*-

from django.forms import ModelForm

from noticias.models import Noticia

class NoticiaForm(ModelForm):

    class Meta():
        model = Noticia
        exclude = ('pub_date',)
