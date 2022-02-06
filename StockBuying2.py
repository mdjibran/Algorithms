
import sys


def StockBuying(lst: list[int]):
    max_profit, min_price = 0.0, float('inf')

    for p in lst:
        today_profit = p - min_price
        max_profit = max(max_profit, today_profit)
        min_price = min(p, min_price)
    
    return max_profit





#print(StockBuying([12,11,13,9,12,8,14,13,15]))
#print(StockBuying([1,2,3,4,5]))
print(StockBuying([310,310,275,275,260,260,260,230,230,230]))
        
'''
def StockBuying(prices):

    slow = 0
    fast = 1
    profit = 0
    shareCount = 0
    sale = False
        
    buy = sys.maxsize
    sell = sys.maxsize * -1
        
    while fast < len(prices):
        if prices[slow] < prices[fast] and shareCount == 0:
            shareCount = 1
            buy = prices[slow]
            sale = False
        elif prices[slow] > prices[fast] and shareCount == 1:
            shareCount = 0
            sell = prices[slow]
            sale = True
          
        if sale:
            print(f"Buy: {buy}, Sell: {sell}, Difference: {sell-buy}")
            profit += (sell-buy)
        slow, fast = slow+1, fast+1
            
    if sale:

    return profit
'''