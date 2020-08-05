class Vehicle:
    engine = True
    def __init__(self,vehicle_seats):
        self.seats = vehicle_seats
        print(f'The vehicle is created an it has {self.seats}')
    def move(self):
       print(f'Vehicle in motions ! ')



class Car:
 # '''This is the parent class car'''
  wheels = 4
  steering_wheel = True
  def __init__(self,car_price,car_brand , car_type):
      # the _ means that it is the protected variable
      self._price = car_price
      self._brand = car_brand
      self._type = car_type
  def braking (self):
      print(f'The car is breaking overthere')
  def print_specs(self):
      print(self._price)
      print(self._type)
      print(self._brand)


def move(automobile):
    automobile.move()








class RaceCar(Car):
    ## This is the blueprint for a race a car
    manfacturer = 'USA'
    rating = 5
    def __init__(self,car_speed, car_sound , car_size, car_hp, car_torque ,price , brand , type):
        super().__init__(price,brand,type)
        ## This is the constructor for RaceCa
        self.speed = car_speed
        self.sound = car_sound
        self.size  = car_size
        self.hp = car_hp
        self.torque  = car_torque
        self.__retailprice = 250000
# This is the override method in the class
    def print_specs(self):
        print(f'\nSpeed: {self.speed}')
        print(f'Engine size : {self.size}')
        print(f'Horsepower: {self.hp}')
        print(f'Torque: {self.torque}')
        # have to makr that it is the protected attributes
        print(f'The price : {self._price}')
        print(f'Brand : {self._brand}')
        print(f'Vehicle type : {self._type}')
    def get_retail(self):
        """This is the getter function to get the retail value """
        return self.__retailprice
    def set_retail(self,value):
        """ This the setter function to set the retail value  """
        self.__retailprice = value


## how to use subclass overe here

mustang_car = Car(200,'BENZ','CAR')
mustang = RaceCar(200,'vroom',569,600,400,1000,'benz' , 'Sedan')
Camry =Car(200 , 'Camary' , 'Sedan')
Bus = Vehicle(50)
mustang.print_specs()
#The are two different print
mustang_car.print_specs()
Camry.print_specs()

# Use the move interface
Bus.move()
move(Bus)

