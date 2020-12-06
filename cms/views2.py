from django.views.generic import TemplateView, ListView, DetailView, CreateView #汎用ビューら
from .models import Book, Recruit, Entry # DB
from django.shortcuts import render

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
