"""
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////

29 March 2023 - Attempt 1
"""

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0
    
    for item in order.items:
        if item.type == 'payment':
            net += item.amount
        elif item.type == 'product':
            net -= item.amount * item.quantity
        else:
            return("Invalid item type: %s" % item.type)
    
    if net != 0:
        return f'Order ID: {order.id} - Payment imbalance: ${net:0.2f}' 
    else:
        return f'Order ID: {order.id} - Full payment received!'
