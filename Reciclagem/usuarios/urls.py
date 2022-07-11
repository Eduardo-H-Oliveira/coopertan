from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('entrar/', auth_views.LoginView.as_view(
         template_name='usuarios/form.html'
     ), name="login"),
     path('sair/', auth_views.LogoutView.as_view(), 
     name='logout')
]
