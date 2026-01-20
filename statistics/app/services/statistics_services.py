from client.orders import get_order_items
from client.master_data import get_menu_items

class MostSoldItems():
    def most_sold_items(self, start_date, end_date):
        menu = get_menu_items() # array -> objets (key=id) -> food_name: str ; price: int
        orders = get_order_items() # array -> objects (key=id) -> food_names: array(str) ; time of the order

        # time: (date [datetime])

        most_sold_items_list = {} # item_name: quantity
        
        # change it to only items sold inbetween the startdate and enddate!

        for order in orders:
            for food_name in order["food_names"]:
                if food_name in most_sold_items_list:
                    most_sold_items_list[food_name] += 1
                else:
                    most_sold_items_list[food_name] = 1
        
        menu_prices = { # foodname: price
            m["food_name"]: m["price"]
            for m in menu
        }
        
        # return a list of objects [{foodname: quant; reevenu}]