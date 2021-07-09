class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.odometer_reading = 0
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''This is a brief description of this function.'''
        """Return a neatly formatted descriptive name."""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
