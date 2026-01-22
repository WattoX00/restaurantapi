from client.orders import get_order_items
from client.master_data import get_menu_items
from collections import defaultdict
from schemas.statistics_schemas import StarDate, EndDate
from interface.statistics_interface import CheckTime

class MostSoldItems(CheckTime):
    def most_sold_items(self, start_date: StarDate, end_date: EndDate):
        menu = get_menu_items()   # [{food_name: str, price: int}]
        orders = get_order_items()  # [{food_names: [str], time: datetime}]

        # food_name -> quantity sold
        sold_count = defaultdict(int)

        # filter orders by date range
        for order in orders:
            order_time = order["time"]
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
            order_time = order["time"]
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
    
class MonthlyData:
    def monthly_data(self):
        pass
