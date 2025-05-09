
from ShoppingCart import ShoppingCart


class CookieCutter:
    def __init__(self, shape, frosting_color, sprinkles, flavor, quantity):
        # these are my default attributes
        # we say self.some attribute = attribute because we don't know what it will be
        self.shape = shape
        self.frosting_color = frosting_color
        self.sprinkles = sprinkles
        self.flavor = flavor
        self.quantity = quantity


# These are different cupcakes (instances)
cupcake1 = CookieCutter("Star Shape","yellow", "while", "vanilla", 50)
cupcake2 = CookieCutter("Heart Shape","white", "red", "Chocolate", 100)
cupcake3 = CookieCutter("circle Shape","strawberry", "purple", "Mochi", 25)

# Each instance holds its own data
print("This is an instance of a cookie made from the CookieCutter Class that has a Shape attribut of a ", cupcake1.shape) # star Shape
print(cupcake2.frosting_color) # red
print(cupcake3.sprinkles)      # 25

