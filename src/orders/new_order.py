import pywmapi as wm
from src import auth
from src.utils.helpers import to_url_name
from typing import Optional

def create_order(item_name: str, order_type: wm.common.OrderType, platinum: int, quantity: int,
                 visible: bool = True, subtype: Optional[str] = None, rank: Optional[int] = None):
    """

       Create a new order on Warframe Market.
    
       Args:
              item_name (str): The name of the item to create an order for.
              order_type (wm.common.OrderType): The type of order (buy/sell) use wm.common.OrderType.sell or wm.common.OrderType.buy.
              platinum (int): The price in platinum.
              quantity (int): The quantity of the item.
              visible (bool, optional): Whether the order is visible. Defaults to True.
              subtype (Optional[str], optional): The subtype of the relic, if applicable (Intact, Exceptional, Flawless, Radiant). Defaults to None.
              rank (Optional[int], optional): The rank of the item, if applicable (0-10). Defaults to None.

         Returns:
              None

    """
    sess = auth.authenticate()

    item_name = to_url_name(item_name)
    data = wm.items.get_item(item_name)[0]
    item_id = data.id
    try:
        new_item = wm.orders.OrderNewItem(
            item_id=item_id,
            order_type=order_type,
            platinum=platinum,
            quantity=quantity,
            subtype=subtype,
            rank=rank,
            visible=visible
        )
    except Exception as e:
        print(f"Error creating order: {e}")
        return

    new_order = wm.orders.add_order(sess, new_item)
    print("Order created sucessfully")
