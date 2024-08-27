from django.urls import path

from ecommerce.views.add_item_to_basket import AddItemToBasketView
from ecommerce.views.categories import CategoriesView
from ecommerce.views.category_item import CategoriesItemsView
from ecommerce.views.checkout_basket import CheckoutBasketView
from ecommerce.views.item import ItemsView

urlpatterns = [
    path('add-item-to-basket', AddItemToBasketView.as_view(), name='add-item-to-basket'),
    path('checkout-basket', CheckoutBasketView.as_view(), name='checkout-basket'),
    path('categories', CategoriesView.as_view(), name='categories'),
    path('items/<str:pk>', ItemsView.as_view(), name='items'),
    path('categories/<str:pk>', CategoriesItemsView.as_view(), name='categories-items'),
]
