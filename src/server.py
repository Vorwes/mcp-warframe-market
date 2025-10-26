from mcp.server.fastmcp import FastMCP
from src.orders.new_order import create_order
import pywmapi as wm
from typing import Optional

mcp = FastMCP("warframe_market")

@mcp.tool()
def create_new_order(item_name: str, order_type: wm.common.OrderType, platinum: int, quantity: int,
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
    create_order(item_name, order_type, platinum, quantity, visible, subtype, rank)

if __name__ == "__main__":
    mcp.run(transport="stdio")
