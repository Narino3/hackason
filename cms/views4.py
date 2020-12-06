#from django.views.generic import TemplateView, ListView, DetailView #汎用ビューら
from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from .models import Book, Recruit, Entry # DB

#class ZibunView(TemplateView):
#    template_name = "cms/zibun.html"

#汎用ビュー
#class MemberList(ListView):
#    model = Entry

def ZibunView(request):
    data = Entry.objects.all()
    params = {'page_type': 0, 'data': data}
    return render(request, 'cms/zibun.html', params)

def ZibunRegistration(request, arg_recruit_ID, arg_entry_ID):
    recruit = Recruit.objects.get(recruit_ID=arg_recruit_ID)
    recruit.finish_flag = True
    entry = Entry.objects.get(entry_ID=arg_entry_ID)
    entry.finish_flag = True
    params = {'page_type': 1, 'data': entry}
    return render(request, 'cms/zibun.html', params)

#def zibun(request):
#    template = loader.get_template('cms/zibun.html')
    #data = Entry.objects.all()
#    params = {'message': 'test message'}
#    return HttpResponse(template.render(params, request))