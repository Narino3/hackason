from django.views.generic import TemplateView, ListView, DetailView, CreateView #汎用ビューら
from .models import *
from django.shortcuts import render

from .forms import OuboForm

#汎用ビュー
class OuboView(ListView):
    template_name = "cms/oubo.html"
    model = Entry

class OuboFinView(ListView):
    template_name = "cms/oubofin.html"
    model = Entry

class TopView(ListView):
    template_name = "cms/Top.html"
    model = Entry

class OuboPutView(CreateView):
    template_name = 'cms/oubo.html' #
    model = Entry
    form_class = OuboForm #このフォーム使用
    #'自動：recruit_ID',  'post_time'
    #fields = ['person_type', 'person_number', 'comment']
    success_url = "/oubofin"