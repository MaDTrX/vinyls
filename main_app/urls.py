#* import path
from django.urls import path
#? what does the dot mean? = refering to the root directory /views
from . import views


urlpatterns = [
    #TODO create home function in views.py
    #TODO refer name=home(kwarg) in template
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls_index, name='index')
    #* path method take in 3 args and the last is opt
]
