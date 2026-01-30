from django.urls import path
from orders.api.views import OrderCreateView, OrderDetailView, OrderCancelView,\
    OrderListView, OrderDetailView


app_name = 'orders'

urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="create_order"),
    path("", OrderListView.as_view(), name="orders_list_create"),
    # path("<uuid:order_id>/", OrderDetailView.as_view()),
    path("<uuid:order_id>/", OrderDetailView.as_view(), name="orders_detail"),
    path("<uuid:order_id>/cancel/", OrderCancelView.as_view(), name="cancel_order"),
]


