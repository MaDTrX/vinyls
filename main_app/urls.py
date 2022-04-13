#* import path
from django.urls import path
#? what does the dot mean? = refering to the root directory /views
from . import views
#TODO 
#!
#*

urlpatterns = [
    #TODO create home function in views.py
    #TODO refer name=home(kwarg) in template
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls_index, name='index'),
    path('vinyls/<int:vinyl_id>', views.vinyls_detail, name='detail'),
    path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
    path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyls_update'),
    path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
    path('vinyls/<int:vinyl_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    #* path method take in 3 args and the last is opt
]
