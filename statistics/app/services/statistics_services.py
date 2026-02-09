from client.orders import get_order_items
from client.master_data import get_menu_items
from collections import defaultdict
from schemas.statistics_schemas import StarDate, EndDate, Year, Month, time_of_day
from interface.statistics_interface import CheckTime

# outside imports
from datetime import datetime
from datetime import date
import calendar

class MostSoldItems(CheckTime):
    def most_sold_items(self, start_date: StarDate, end_date: EndDate):
        menu = get_menu_items()   # [{food_name: str, price: int}]
        orders = get_order_items()  # [{food_names: [str], time: datetime}]

        # food_name -> quantity sold
        sold_count = defaultdict(int)

        # filter orders by date range
        for order in orders:
            order_time = datetime.fromisoformat(order["time"]).date()
            if start_date <= order_time <= end_date:
                for food_name in order["food_names"]:
                    sold_count[food_name] += 1

        # food_name -> price
        menu_prices = {
            m["food_name"]: m["price"]
            for m in menu
        }

        # build result list
        result = []
        for food_name, quantity in sold_count.items():
            price = menu_prices.get(food_name, 0)
            result.append({
                "food_name": food_name,
                "quantity": quantity,
                "revenue": quantity * price
            })

        # optional: sort by quantity sold (descending)
        result.sort(key=lambda x: x["quantity"], reverse=True)

        return result

class LeastItemsSold(CheckTime):
    def least_items_sold(self, start_date: StarDate, end_date: EndDate ):
        menu = get_menu_items()
        orders = get_order_items()

        sold_count = defaultdict(int)

        for order in orders:
            order_time = datetime.fromisoformat(order["time"]).date()
            if start_date <= order_time <= end_date:
                for food_name in order["food_names"]:
                    sold_count[food_name] += 1

        menu_prices = {
            m["food_name"]: m["price"]
            for m in menu
        }

        result = []
        for food_name, quantity in sold_count.items():
            price = menu_prices.get(food_name, 0)
            result.append({
                "food_name": food_name,
                "quantity": quantity,
                "revenue": quantity * price
            })

        result.sort(key=lambda x: x["quantity"], reverse=False)

        return result
    
class MonthlyData():
    def monthly_data(self, year: Year, month: Month):
        # number of month comes in -> defines start_date and end_date
        # look for the orders datase in that time period:
            # get total revenue
            # get how much items were sold by the time of the day
        # need monthly salary + the time of the day
    # return {total_revenu: morning:x; noon:x; afternoon:x}

        # date
        month += 1

        start_date = date(year, month, 1)
        last_day = calendar.monthrange(year, month)[1]
        end_date = date(year, month, last_day)

        # menu req
        menu = get_menu_items()   # [{food_name: str, price: int}]
        orders = get_order_items()  # [{food_names: [str], time: datetime}]

        # food_name -> quantity sold; time_of_day(morning;noon;afternoon): str
        sold_count = defaultdict(int)

        # filter orders by date range
        for order in orders:
            order_dt = datetime.fromisoformat(order["time"])
            if start_date <= order_dt.date() <= end_date:
                tod = time_of_day(order_dt)
                for food_name in order["food_names"]:
                    sold_count[(food_name, tod)] += 1

        menu_prices = {
            m["food_name"]: m["price"]
            for m in menu
        }

        revenue_result = 0
        # build result list
        revenue_result = int()
        for (food_name, tod), quantity in sold_count.items():
            price = menu_prices.get(food_name, 0)
            revenue_result += quantity * price
        sold_count_out = [
            {"time_of_day": tod, "quantity": quantity}
            for (food_name, tod), quantity in sold_count.items()
        ]
        return start_date, end_date, revenue_result, sold_count_out

class MonthlyData():
    def monthly_data(self, year: Year, month: Month):
        month += 1

        start_date = date(year, month, 1)
        last_day = calendar.monthrange(year, month)[1]
        end_date = date(year, month, last_day)

        menu = get_menu_items()   # [{food_name: str, price: int}]
        orders = get_order_items()  # [{food_names: [str], time: datetime}]

        sold_count = defaultdict(int)
        revenue_by_tod = defaultdict(int)

        for order in orders:
            order_dt = datetime.fromisoformat(order["time"])
            if start_date <= order_dt.date() <= end_date:
                tod = time_of_day(order_dt)
                for food_name in order["food_names"]:
                    sold_count[(food_name, tod)] += 1

        menu_prices = {m["food_name"]: m["price"] for m in menu}

        total_revenue = 0
        for (food_name, tod), quantity in sold_count.items():
            price = menu_prices.get(food_name, 0)
            revenue = quantity * price
            total_revenue += revenue
            revenue_by_tod[tod] += revenue

        return {
            "total_revenue": total_revenue,
            "morning": revenue_by_tod.get("morning", 0),
            "noon": revenue_by_tod.get("noon", 0),
            "afternoon": revenue_by_tod.get("afternoon", 0)
        }

