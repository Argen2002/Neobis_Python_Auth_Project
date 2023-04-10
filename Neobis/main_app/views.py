from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

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




def login(request):
    return HttpResponse("Login")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>СТраница не найдена</h1>')


class DataMixin:
    pass

#Первый метод из ютуба где обЪеденины регистрация и логин
class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     c_def =self.get



#разделение класов на регистр и логин
class RegisterForm:
    pass


class RegisterView(CreateView):
    form_class=RegisterForm
    template_name='registration/login.html'
    success_url = reverse_lazy('login')
class LoginView(FormView):
    form_class=AuthenticationForm
    template_name='registration/login.html'
    success_url = reverse_lazy('/')



#using  function----------------------------------------------------------------------------
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})