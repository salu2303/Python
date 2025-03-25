from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('quote/', views.create_quote, name='create_quote'),
    path('success/', views.quote_success, name='quote_success'),
    path('get_price/', views.get_price, name='get_price'),

]
