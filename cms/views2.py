from django.views.generic import TemplateView, ListView, DetailView #汎用ビューら
from .models import Book # DB

class OuboView(TemplateView):
    template_name = "cms/index.html"

#汎用ビュー
class MemberList(ListView):
    model = Book