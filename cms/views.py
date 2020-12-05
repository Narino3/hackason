from django.views.generic import TemplateView, ListView, DetailView #汎用ビューら
from .models import Book # DB

class IndexView(TemplateView):
    template_name = "cms/index.html"

    def get_context_data(self):
        ctxt = super().get_context_data() # super はDjangoの元から持っているものを使用
        ctxt["username"] = "あおい"
        return ctxt


class AboutView(TemplateView):
    template_name = "cms/about.html"

    def get_context_data(self):
        ctxt = super().get_context_data() # super はDjangoの元から持っているものを使用
        ctxt["num_services"] = 12345678
        ctxt["skills"] = [
            "Python",
            "C++",
            "Javascript",
            "Rust",
        ]
        return ctxt

class MemberList(ListView):
    model = Book