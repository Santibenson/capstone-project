from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path('menu/<str:pk>', views.SingleMenuItemView.as_view(), name='single_item'),
    path('booking', views.BookingView.as_view(), name='booking')
]