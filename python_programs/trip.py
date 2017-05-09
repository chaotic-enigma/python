def hotel_cost(nights):
    return 140 * nights
print hotel_cost(1234)
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 23245
print plane_ride_cost("kakka")
def rental_car_cost(days):
    total_cost = 40 * days
    if days >= 7:
        total_cost -= 50
    elif days >= 3:
        total_cost -= 20
    return total_cost
print rental_car_cost(2)
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print ("The trip cost to Los Angeles is: %d") % trip_cost("Los Angeles", 5, 600) 
