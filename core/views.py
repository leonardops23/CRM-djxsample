from django.views.generic import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {
            'titulo': 'Home'
        }
        return render(request, 'index.html', context)

class AboutUs(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {
            'titulo': 'About Us'
        }
        return render(request, 'navegations/about_us.html', context)
