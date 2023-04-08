from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *

# Create your views here.
menu = ["About us", "Add state", "Feedback", "Join"]

def index(request):
    posts=main_app.objects.all()
    # context = {
    #     'posts': posts,
    #     'menu': menu,
    #     'title': 'Main page'
    # }
    return render(request, 'main_app/index.html', {'posts':posts, 'menu':menu, 'title': 'main page'})


def about(request):
    return render(request, 'main_app/about.html',{'menu':menu,'title': 'about us'})

def categories(request, catid):
    if(request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>Pafe of app main_app</h1><p>{catid}</p>")

def archive(request,year):
    if int(year)>2020:
        return redirect('home',permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def login(request):
    return HttpResponse("Login")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>СТраница не найдена</h1>')


class DataMixin:
    pass


#19-lesson class RegisterUser(DataMixin,CreateView):
#     form_class = UserCreationForm
#     template_name = 'main_app/register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context= supper().get_context_data(**kwargs)