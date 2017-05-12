class Artificial_intelligence(object):
	def __init__(self, branch, background, father):
		self.branch = branch
		self.background = background
		self.father = father

	def description(self):
		print 'Artificial Intelligence is a newly discovered by %s, one of the fields in %s and it has several branches: one of the branches is %s.' % (self.father, self.background, self.branch)

ai = Artificial_intelligence('Machine_learning', 'Computer_science', 'Alan_turing')
print ai.description()
print 

#example of global variables in classes
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive
print 

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = 'good'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
       print self.name
       print self.age
    
hippo = Animal('hippopotamus', 23)
print hippo.description()
print hippo.health
sloth = Animal('eagle', 100)
print sloth.description()
print sloth.health
ocelot = Animal('pig', '3 days')
print ocelot.description()
print ocelot.health
print 

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."
my_cart = ShoppingCart('jarvis')
my_cart.add_item('nuclear_reactor', 1000)
print

#inheritance class
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
print 

class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

    def description_old(self):
    	print 'The no: of sides are: %s' % (self.number_of_sides)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def description_sides(self):
    	print 'My sides are %scm, %scm %scm' % (self.side1, self.side2, self.side3)

number = Shape(3)
number.description_old()
triangle = Triangle(3, 3, 3)
triangle.description_sides()
print
        
#override
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
pte = PartTimeEmployee('Steve')
emp = Employee('mj')
print emp.calculate_wage(12)
print pte.calculate_wage(21)
print 

#return using 'super()' call
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        self.hours = hours
        return hours * 20.00
        return super(PartTimeEmployee, self).full_time_wage()
        
milton = PartTimeEmployee('Bob')
print milton.full_time_wage(10)
pte = PartTimeEmployee('Steve')
emp = Employee('mj')
print emp.calculate_wage(12)
print pte.calculate_wage(21)
print 

#final code
class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else: 
            False

my_triangle = Triangle(90, 30, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
    angle = 60
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
    def check_equilateral(self):
        if self.angle1 == self.angle and self.angle2 == self.angle and self.angle3 == self.angle:
            return 'Equilateral'
        else:
            return 'not an equilateral'

equal = Equilateral(60, 60, 60)
print equal.number_of_sides
print equal.check_equilateral()
print 

