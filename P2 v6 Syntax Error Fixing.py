def CoS():
    opening_stock = 5
    purchases = 5
    closing_stock = 7
    global cost_of_sales
    cost_of_sales = opening_stock + purchases - closing_stock
    return cost_of_sales

CoS()
print cost_of_sales
