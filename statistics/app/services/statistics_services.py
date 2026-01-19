from client.orders import get_order_items
from client.master_data import get_menu_items

class MostSoldItems():
    def most_sold_items(self):
        menu = get_menu_items() # array -> objets (key=id) -> food_name: str ; price: int
        orders = get_order_items() # array -> objects (key=id) -> food_names: array(str)

        most_sold_items_list = {} # item_name: quantity

        for order in orders:
            for food_name in order["food_names"]:
                if food_name in most_sold_items_list:
                    most_sold_items_list[food_name] += 1
                else:
                    most_sold_items_list[food_name] = 1
        
        menu_prices = {
            m["food_name"]: m["price"]
            for m in menu
        }

        revenue_by_item = {}

        for item_name, quantity in most_sold_items_list.items():
            price = menu_prices.get(item_name)

            if price is None:
                continue

            revenue_by_item[item_name] = quantity * price

        return revenue_by_item
