from django.urls import path
from orders.api.views import OrderCreateView, OrderDetailView, OrderCancelView


app_name = 'orders'

urlpatterns = [
    path("", OrderCreateView.as_view()),
    path("<uuid:order_id>/", OrderDetailView.as_view()),
    path("<uuid:order_id>/cancel/", OrderCancelView.as_view()),
]

