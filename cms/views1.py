from django.views.generic import TemplateView, ListView, DetailView #汎用ビューら
from .models import * # DB
from django.shortcuts import render

#class RecruitView(ListView):
#    model = Recruit
#    template_name = "cms/index.html"

    #model = Recruit
    #queryset = Recruit.objects.all()
    #def function(request):
    #	context={"data" : Recruit.objects.all()}
	#	return render(request, 'cms/index.html', context)
#汎用ビュー
class MemberList(ListView):
    model = Recruit

def list(request):
    data = Recruit.objects.all()
    params = {'message': 'メンバーの一覧', 'data': data}
    return render(request, 'cms/index.html', params)