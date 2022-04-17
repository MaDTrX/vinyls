#* import path
from django.urls import path
from . import views
from .views import PartyList, PartyCreate, PartyDelete, PartyUpdate, PartyDetail

#TODO 
#!
#*

urlpatterns = [
    #TODO create home function in views.py
    #TODO refer name=home(kwarg) in template
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls_index, name='index'),
    path('vinyls/<int:vinyl_id>/', views.vinyls_detail, name='detail'),
    path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
    path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyls_update'),
    path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
    path('vinyls/<int:vinyl_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('vinyls/<int:vinyl_id>/add_photo/', views.add_photo, name='add_photo'),
    path('vinyls/<int:vinyl_id>/assoc_party/<int:party_id>/', views.assoc_party, name='assoc_party'),
    path('vinyls/<int:vinyl_id>/unassoc_party/<int:party_id>/', views.unassoc_party, name='unassoc_party'),
    path('parties/', PartyList.as_view(), name='parties_index'),
    path('parties/<int:pk>/', PartyDetail.as_view(), name='parties_detail'),
    path('parties/create/', PartyCreate.as_view(), name='parties_create'),
    path('parties/<int:pk>/update/', PartyUpdate.as_view(), name='parties_update'),
    path('parties/<int:pk>/delete/', PartyDelete.as_view(), name='parties_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    #* path method take in 3 args and the last is opt
]
