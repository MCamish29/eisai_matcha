from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='products'),
    path('tea/', views.tea, name='tea'),  # Ensure this is correctly mapped
]
