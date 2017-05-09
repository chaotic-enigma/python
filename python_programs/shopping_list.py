shopping_list = ["banana", "orange", "apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
} 
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def compute_bill(food):
    total = 0
    for each_item in food:
        if stock[each_item] > 0:
            total += prices[each_item]
            stock[each_item] -= 1
    return total    
print "Total cost is %f" % compute_bill(shopping_list)