# from django.urls import path
# from django.conf.urls import include
# from django.conf.urls.static import static
# from project_moneyBank import settings
# from moneyBank.views import about, contact, home, make_transaction_filled, transfer, view_all_customers, view_customer, view_transactions, view_transactions_page, view_your_account_details, view_your_account_details_page

# urlpatterns = [
#     url('home/$', home),
#     url('view_all_customers/$', view_all_customers),
#     path('view_customer/<user2>/', view_customer),
#     path('make_transaction_field/<user2>/', make_transaction_filled),
#     url('transfer/$', transfer),
#     url('view_your_account_details/$', view_your_account_details),
#     url('view_your_account_details_page/$', view_your_account_details_page),
#     url('view_transactions_page/$', view_transactions_page),
#     url('view_transactions/$', view_transactions),
#     url('contact/$', contact),
#     url('about/$', about),
# ]

from django.urls import path, include  # Use only path() & include()
from django.conf import settings
from django.conf.urls.static import static
from moneyBank.views import (
    about, contact, home, make_transaction_filled, transfer, 
    view_all_customers, view_customer, view_transactions, 
    view_transactions_page, view_your_account_details, view_your_account_details_page
)

urlpatterns = [
    path('', home, name='home'),  
    path('view_all_customers/', view_all_customers, name='view_all_customers'),  
    path('view_customer/<str:user2>/', view_customer, name='view_customer'),  
    path('make_transaction_field/<str:user2>/', make_transaction_filled, name='make_transaction_filled'),  
    path('transfer/', transfer, name='transfer'),  
    path('view_your_account_details/', view_your_account_details, name='view_your_account_details'),  
    path('view_your_account_details_page/', view_your_account_details_page, name='view_your_account_details_page'),  
    path('view_transactions_page/', view_transactions_page, name='view_transactions_page'),  
    path('view_transactions/', view_transactions, name='view_transactions'),  
    path('contact/', contact, name='contact'),  
    path('about/', about, name='about'),  
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
