from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404

from orders.models import Order
from orders.services.exceptions import (
    OrderNotFound,
    InvalidOrderState,
)


User = get_user_model()


def create_order(*, user: User, amount: int) -> Order:
    """
    Create a new order in PENDING state
    """
    return Order.objects.create(
        user=user,
        amount=amount,
        status=Order.Status.PENDING,
    )




def get_order(*, order_id):
    try:
        return Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        raise OrderNotFound



@transaction.atomic
def start_processing(*, order_id) -> Order:
    """
    Move order from PENDING -> PROCESSING
    """
    try:
        order = Order.objects.select_for_update().get(id=order_id)
    except Order.DoesNotExist:
        raise OrderNotFound()


    if order.status == Order.Status.CANCELED:
        return order
    

    if order.status != Order.Status.PENDING:
        raise InvalidOrderState(
            f"Cannot start processing from state {order.status}"
        )

    order.status = Order.Status.PROCESSING
    order.save(update_fields=["status", "updated_at"])

    return order


@transaction.atomic
def complete_order(*, order_id) -> Order:
    """
    Move order from PROCESSING -> COMPLETED
    """
    try:
        order = Order.objects.select_for_update().get(id=order_id)
    except Order.DoesNotExist:
        raise OrderNotFound()


    if order.status == Order.Status.CANCELED:
        return order

    if order.status != Order.Status.PROCESSING:
        raise InvalidOrderState(
            f"Cannot complete order from state {order.status}"
        )
        
    order.status = Order.Status.COMPLETED
    order.save(update_fields=["status", "updated_at"])

    return order


@transaction.atomic
def fail_order(*, order_id, reason=None) -> Order:
    """
    Move order from PROCESSING -> FAILED
    """
    try:
        order = Order.objects.select_for_update().get(id=order_id)
    except Order.DoesNotExist:
        raise OrderNotFound()

    if order.status != Order.Status.PROCESSING:
        raise InvalidOrderState(
            f"Cannot fail order from state {order.status}"
        )

    order.status = Order.Status.FAILED
    if reason:
        if order.metadata:
            order.metadata.update({"failure_reason": reason})
        else:
            order.metadata = {"failure_reason": reason}

    order.save(update_fields=["status", "metadata", "updated_at"])

    return order


@transaction.atomic
def cancel_order(*, order_id):
    """
    Cancel an order if busuness rules allow it.
    This operation is idempotent.
    """
    
    try :
        order = Order.objects.select_for_update().get(id=order_id)
    except Order.DoesNotExist:
        raise OrderNotFound()
    
    if order.status == Order.Status.CANCELED:
        return order
    
    if order.status not in [Order.Status.PENDING, Order.Status.PROCESSING] :
        raise InvalidOrderState(f"Order cannot be canceled while in '{order.status}' state.")
    
    order.status = Order.Status.CANCELED
    order.save(update_fields=['status', 'update_at'])
    return order