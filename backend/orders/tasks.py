import random
from celery import shared_task

from orders.services.order_service import (
    start_processing,
    complete_order,
    fail_order,
)
from orders.services.exceptions import InvalidOrderState, OrderNotFound


FAIL_RATE = 0.2
PROCESSING_DELAY = 5  # seconds


@shared_task(bind=True)
def process_order_task(self, order_id: str):
    try:
        start_processing(order_id=order_id)

        should_fail = random.random() < FAIL_RATE

        finalize_order_task.apply_async(
            args=[order_id, should_fail],
            countdown=PROCESSING_DELAY,
        )

    except (InvalidOrderState, OrderNotFound):
        raise


@shared_task(bind=True)
def finalize_order_task(self, order_id: str, should_fail: bool):
    try:
        if should_fail:
            fail_order(
                order_id=order_id,
                reason="Simulated processing failure",
            )
        else:
            complete_order(order_id=order_id)

    except (InvalidOrderState, OrderNotFound):
        raise


