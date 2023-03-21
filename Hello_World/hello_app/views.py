from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name = "hello_app\home.html"
