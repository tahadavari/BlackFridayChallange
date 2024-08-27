from django.urls import path

urlpatterns = [
    path('add-item-to-basket', ),
    path('checkout-basket', ),
    path('categories', ),
    path('items/<int:id>', ),
    path('categories/<str:category>', ),
]
