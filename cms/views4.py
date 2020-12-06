#from django.views.generic import TemplateView, ListView, DetailView #汎用ビューら
from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from django import forms
from .models import Book, Recruit, Entry # DB

#class ZibunView(TemplateView):
#    template_name = "cms/zibun.html"

#汎用ビュー
#class MemberList(ListView):
#    model = Entry

def ZibunView(request):
    if request.method == 'POST':
        arg_recruit_ID = request.POST['zibun_recruit_ID']
        arg_entry_ID = request.POST['zibun_entry_ID']
        arg_recruit = Recruit.objects.get(recruit_ID=arg_recruit_ID)
        arg_recruit.finish_flag = True
        arg_entry = Entry.objects.get(entry_ID=arg_entry_ID)
        arg_entry.finish_flag = True

    arg_recruit_ID = 1
    recruit = Recruit.objects.get(recruit_ID=arg_recruit_ID)
    entries = Entry.objects.filter(recruit_ID=arg_recruit_ID)
    #entries = recruit.entry.all().order_by('entry_ID')
    matching_entries = entries.filter(finish_flag=True)
    params = {'page_type': 0, 'recruit': recruit, 'entries': entries, 'matching_entries': matching_entries}
    return render(request, 'cms/zibun.html', params)

#def post(request):
#    arg_recruit_ID = request.POST['zibun_recruit_ID']
#    arg_entry_ID = request.POST['zibun_entry_ID']
#    recruit = Recruit.objects.get(recruit_ID=arg_recruit_ID)
#    recruit.finish_flag = True
    #entries = Entry.objects.filter(recruit_ID=arg_recruit_ID)
#    entries = recruit.entry.all().order_by('entry_ID')
#    entry = Entry.objects.get(entry_ID=arg_entry_ID)
#    entry.finish_flag = True
#    matching_entries = entries.filter(finish_flag=True)
#    params = {'page_type': 1, 'recruit': recruit, 'entries': entries, 'matching_entries': matching_entries}
#    return render(request, 'cms/zibun.html', params)

#def ZibunRegistration(request, arg_recruit_ID, arg_entry_ID):
#    recruit = Recruit.objects.get(recruit_ID=arg_recruit_ID)
#    recruit.finish_flag = True
#    entry = Entry.objects.get(entry_ID=arg_entry_ID)
#    entry.finish_flag = True
#    params = {'page_type': 1, 'data': entry}
#    return render(request, 'cms/zibun.html', params)

#def zibun(request):
#    template = loader.get_template('cms/zibun.html')
    #data = Entry.objects.all()
#    params = {'message': 'test message'}
#    return HttpResponse(template.render(params, request))
