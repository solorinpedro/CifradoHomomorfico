from django.urls import path, re_path
from django.views.generic.base import RedirectView
from persona import views
from persona.views import consultar_personas, crear_personas  

urlpatterns = [
    
    path('', views.home, name='home'),
    path('crear/', crear_personas, name='crear_personas'),
    path('consultar/', consultar_personas, name='consultar_personas'),
]