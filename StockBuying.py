import sys

def StockBuying(lst):
    buy = sys.maxsize
    sell = sys.maxsize*-1
    low = 0
    high = len(lst) -1


    while low <= high:
        buy = min(lst[low], buy)
        sell = max(lst[high], sell)
        low, high = low +1, high -1
    
    return (buy, sell)






print(StockBuying([310,315,275,295,260,270,290,230,255,250]))