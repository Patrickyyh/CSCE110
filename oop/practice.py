class Shape:
   default_color = 'blue'
   # New: Add class variable
   background_color = 'black'

   def __init__(self):
      self.color = self.default_color

   # New: Add class method
   def print_description(self):
      print(self.color, 'on', self.background_color)


a_shape = Shape()
a_shape.print_description()

a_shape.color = 'tan'
a_shape.print_description()

Shape.background_color = 'ivory'
a_shape.print_description()
