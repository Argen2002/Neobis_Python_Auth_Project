from django.urls import path,re_path

from .views import (
    index,
    about,
    RegisterUser,
    RegisterView,
    LoginView,
    register_view,
    login_view
)

urlpatterns = [
    path('',index, name='home'),

    path('about/' , about , name='about'),

    path('accounts/register/',RegisterUser.as_view(),name='register'),

    path('secondregistr/',RegisterView.as_view(),name='secondregistr'),

    path('secondlogin/',LoginView.as_view(),name='secondlogin'),

    #function------------
    path('funregister/', register_view, name='funregister'),
    path('funlogin/', login_view, name='funlogin'),

]

