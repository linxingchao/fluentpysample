from abc import ABC,abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple,Optional

class Customer(NamedTuple):
    name:str
    fidelity:int
    
class LineItem(NamedTuple):
    product:str
    quanlity:int
    price:Decimal
    
    def total(self) -> Decimal:
        return self.price * self.quanlity
    
class Order(NamedTuple):
    customer:Customer
    cart: Sequence[LineItem]
    promotion: Optional['Promotion'] = None
    
    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals,start=Decimal(0))
    
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        return f'<Order total:{self.total():0.2f} due:{self.due():.2f}>'
    
class Promotion(ABC):
    @abstractmethod
    def discount(self,order:Order) -> Decimal:
        pass
    
class FidelityPromo(Promotion):
    """为积分1000或以上的顾客提供5%的折扣"""
    
    def discount(self, order: Order) -> Decimal:
        rate = Decimal('0.05')
        if order.customer.fidelity >= 1000:
            return order.total() * rate
        return Decimal(0)
    
class BulkItemPromo(Promotion):
    """为单个商品数量20个或以上提供10%折扣"""
    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quanlity >= 20:
                discount += item.total() * Decimal('0.1')
            return discount    
        
class LargOrderPromo(Promotion):
    """订单中不同商品数量达到10或以上时，提供7%的折扣"""
    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * Decimal('0.07')
        return Decimal(0)
