from django.urls import path
from orders.api.views import OrderCreateView, OrderDetailView, OrderCancelView

# from .views import health_check


urlpatterns = [
    # path("health/", health_check, name="health_check"),
    path("orders/", OrderCreateView.as_view()),
    path("orders/<uuid:order_id>/", OrderDetailView.as_view()),
    path("orders/<uuid:order_id>/cancel/", OrderCancelView.as_view()),
]


# urlpatterns += [
#     path("health/", HealthCheckView.as_view()),
# ]
