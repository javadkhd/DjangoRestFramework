import math


def run_cpu_heavy_job(order_id: str) -> None:
    """
    Simulate real CPU-bound work
    """
    # Do everything that need a lot of time
    
    result = 0
    for i in range(1, 50_000_000):
        result += math.sqrt(i)


