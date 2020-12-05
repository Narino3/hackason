from django.views.generic import TemplateView, ListView, DetailView, CreateView #汎用ビューら
from django.urls import reverse

#from django.shortcuts import render, get_object_or_404, redirect #form
#from cms.forms import BosyuForm

from .models import * # DB
from .forms import BosyuForm

from django.http import HttpResponse
from django.utils import timezone

#汎用ビュー
class ModelList(ListView):
    template_name = 'cms/hyouzi.html' #
    model = Recruit
    #model = Book

class BosyuView(CreateView):
    template_name = 'cms/bosyu.html' #
    model = Recruit
    form_class = BosyuForm #このフォーム使用
    #'自動：recruit_ID',  'post_time'
    #fields = ['recruit_title', 'shop_ID', 'finish_time', 'person_type', 'person_number', 'work_start_time', 'work_last_time','comment', 'finish_time', 'password']
    success_url = "/bosyufin"
#    def get_success_url(self):
#        return reverse('oubo', kwargs={'pk': self.object.pk})

class BosyuFinView(ListView): # ここでDBの処理
    template_name = 'cms/bosyufin.html'
    model = Recruit

class setView(CreateView):
    template_name = 'cms/set_tag.html' #
    model = PType
    fields = ['pty']
    success_url = "."