class Car():
    """Prosta próba zaprezentowania samochodu."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu!")
    
    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers

class Battery():
    """Prosta próba modelowania akumulatora samochodu elektrycznego."""

    def __init__(self, battery_size=75):
        """Inicjalizacja atrybutów akumulatora."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora."""
        print(f"Ten samochód ma akumulator o pojemności {self.battery_size} kWh.")

    def get_range(self):  
        """
        Wyświetla informacje o zasięgu samochodu na podstawie pojemności akumulatora.
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"Zasięg tego samochodu wynosi około {range} km po pełnym naładowaniu akumulatora.")


class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """
        Inicjalizacja atrybutów klasy nadrzędnej.
        Nastęnie inicjalizacja atrybutów charakterystycznych
        dla samochodu elektrycznego.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora."""
        print(f"Ten samochód ma akumulator o pojemności {self.battery_size} kWh.") 

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()