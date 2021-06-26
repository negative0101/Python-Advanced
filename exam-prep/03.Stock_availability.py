from collections import deque


def stock_availability(list_of_products, actions='', *args):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    stocks = list_of_products
    if actions == 'delivery':
        if args:
            for i in range(len(args)):
                stocks.append(args[i])
            return stocks
    elif actions == 'sell':
        if args:
            try:
                if args[0] in numbers:
                    for i in range((args[0])):
                        deque(stocks.pop(0))
                    return list(stocks)
            except TypeError:
                pass
            finally:
                for item in args:
                    if item in stocks:
                        for i in range(stocks.count(item)):
                            stocks.remove(item)
                return stocks

        else:
            stocks = deque(stocks)
            stocks.popleft()
            return list(stocks)

    return stocks


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
