from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='products'),
    path('tea/', views.tea, name='tea'),
    path('equipment/', views.equipment, name='equipment'),
    path('kits/', views.kit, name='kits'),  
]