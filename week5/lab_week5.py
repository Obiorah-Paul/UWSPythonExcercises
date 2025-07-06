class Vehicle:
    """A base class representing a generic vehicle."""
    def __init__(self, colour: str, weight: int, max_speed: int, **kwargs):
        """Initialize a Vehicle object.
        Args:
            colour (str): The colour of the vehicle.
            weight (int): The weight of the vehicle.
            max_speed (int): The maximum speed of the vehicle.
            **kwargs: Additional keyword arguments (e.g., max_range, seats).
        """
        print("Start Vehicle")
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.max_range = kwargs.get('max_range')
        self.seats = kwargs.get('seats')

    def move(self, speed: int):
        """Move the vehicle at a given speed."""
        print(f"The vehicle is moving at {speed} km/h")

#Inheritance and super()
class Car(Vehicle):
    """A class representing a car, inheriting from Vehicle."""
    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, **kwargs):
        """Initialize a Car object.
        Args:
            colour (str): The colour of the car.
            weight (int): The weight of the car.
            max_speed (int): The maximum speed of the car.
            form_factor (str): The form factor of the car.
            **kwargs: Additional keyword arguments.
        """
        print("Start Car")
        super().__init__(colour, weight, max_speed, **kwargs)
        self.form_factor = form_factor

    def move(self, speed: int):
        """Drive the car at a given speed."""
        print(f"The car is driving at {speed} km/h")

class Electric(Car):
    """A class representing an electric car, inheriting from Car."""
    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, battery_capacity: int, **kwargs):
        """Initialize an Electric car object.
        Args:
            colour (str): The colour of the car.
            weight (int): The weight of the car.
            max_speed (int): The maximum speed of the car.
            form_factor (str): The form factor of the car.
            battery_capacity (int): The battery capacity in kWh.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.battery_capacity = battery_capacity

    def move(self, speed: int):
        """Drive the electric car at a given speed."""
        range_str = f"and has a maximum range of {self.max_range} km" if self.max_range else ""
        print(f"The electric car is driving at {speed} km/h {range_str}")

class Petrol(Car):
    """A class representing a petrol car, inheriting from Car."""
    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, fuel_capacity: int, **kwargs):
        """Initialize a Petrol car object.
        Args:
            colour (str): The colour of the car.
            weight (int): The weight of the car.
            max_speed (int): The maximum speed of the car.
            form_factor (str): The form factor of the car.
            fuel_capacity (int): The fuel capacity in liters.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.fuel_capacity = fuel_capacity

    def move(self, speed: int):
        """Drive the petrol car at a given speed."""
        range_str = f"and has a maximum range of {self.max_range} km" if self.max_range else ""  
        print(f"The petrol car is driving at {speed} km/h {range_str}")

class Plane(Vehicle):
    """A class representing a plane, inheriting from Vehicle."""
    def __init__(self, colour: str, weight: int, max_speed: int, wingspan: float, **kwargs):
        """Initialize a Plane object.
        Args:
            colour (str): The colour of the plane.
            weight (int): The weight of the plane.
            max_speed (int): The maximum speed of the plane.
            wingspan (float): The wingspan of the plane in meters.
            **kwargs: Additional keyword arguments.
        """
        print("Start Plane")
        super().__init__(colour, weight, max_speed, **kwargs)
        self.wingspan = wingspan

    def move(self, speed: int):
        """Fly the plane at a given speed."""
        print(f"The plane is flying at {speed} km/h")

class Propeller(Plane):
    """A class representing a propeller plane, inheriting from Plane."""
    def __init__(self, colour: str, weight: int, max_speed: int, wingspan: float, propeller_diameter: float, **kwargs):
        """Initialize a Propeller plane object.
        Args:
            colour (str): The colour of the plane.
            weight (int): The weight of the plane.
            max_speed (int): The maximum speed of the plane.
            wingspan (float): The wingspan of the plane in meters.
            propeller_diameter (float): The diameter of the propeller.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.propeller_diameter = propeller_diameter

    def move(self, speed: int):
        """Fly the propeller plane at a given speed."""
        print(f"The propeller plane is flying at {speed} km/h")

class Jet(Plane):
    """A class representing a jet plane, inheriting from Plane."""
    def __init__(self, colour: str, weight: int, max_speed: int, wingspan: float, engine_thrust: int, **kwargs):
        """Initialize a Jet plane object.
        Args:
            colour (str): The colour of the jet.
            weight (int): The weight of the jet.
            max_speed (int): The maximum speed of the jet.
            wingspan (float): The wingspan of the jet in meters.
            engine_thrust (int): The engine thrust of the jet.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.engine_thrust = engine_thrust

    def move(self, speed: int):
        """Fly the jet plane at a given speed."""
        print(f"The jet plane is flying at {speed} km/h")

#Multiple Inheritance

class FlyingCar(Car, Plane):
    """A class representing a flying car, inheriting from both Car and Plane."""
    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, wingspan: float, **kwargs):
        """Initialize a FlyingCar object.
        Args:
            colour (str): The colour of the flying car.
            weight (int): The weight of the flying car.
            max_speed (int): The maximum speed of the flying car.
            form_factor (str): The form factor of the flying car.
            wingspan (float): The wingspan of the flying car in meters.
            **kwargs: Additional keyword arguments.
        """
        # We pass all arguments needed by both parent initialisers.
        super().__init__(colour, weight, max_speed, form_factor=form_factor, wingspan=wingspan, **kwargs)

    def move(self, speed: int):
        """Drive or fly the flying car at a given speed."""
        print(f"The flying car is driving or flying at {speed} km/h")


#Polymorphism

generic_vehicle = Vehicle("red", 1000, 200)
electric_car = Electric("green", 1200, 200, "Hatchback", 100, max_range=450)
petrol_car = Petrol("blue", 1500, 250, "SUV", 50, max_range=600, seats=5)
jet_plane = Jet("white", 20000, 900, 35.8, 160, seats=180)
flying_car = FlyingCar("silver", 1800, 300, form_factor="Coupe", wingspan=8.5, seats=2, max_range=500)

# class Animal:
    #"""A simple Animal class to demonstrate polymorphism with unrelated objects."""
    #def move(self, speed: int):
    #    print(f"The animal is moving at a speed of {speed} km/h")

#generic_animal = Animal()

movable_objects = [generic_vehicle, electric_car, petrol_car, jet_plane, flying_car] #generic_animal]


# Loop through the list and call the same method on each object
for item in movable_objects:
    item.move(120)


print(f"Petrol car seats: {petrol_car.seats}")
print(f"Flying car wingspan: {flying_car.wingspan}, form factor: {flying_car.form_factor}")
