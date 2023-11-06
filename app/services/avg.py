import time
from services.helper import p_date
class avg():
    
    def avg_time(orders):
        completed_orders = [order for order in orders if order.status and order.completed_at is not None]
        total = sum(p_date(result.completed_at) - p_date(result.created_at) for result in completed_orders)
        avg = total / len(completed_orders)
        return time.strftime("%H:%M:%S", time.gmtime(avg))
    
    def avg_day(orders):
        completed_orders = [order for order in orders if order.status and order.completed_at is not None]
        unique_dates = set(order.completed_at.date() for order in completed_orders)
        total_completed_orders = len(completed_orders)
        total_days = len(unique_dates)
        return total_completed_orders /total_days
        
