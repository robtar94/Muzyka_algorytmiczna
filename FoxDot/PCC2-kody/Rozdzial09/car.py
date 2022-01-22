class Car():
    """Prosta próba zaprezentowania samochodu."""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących samochód."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Wyświetla informację o przebiegu samochodu."""
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        """
        Przypisanie podanej wartości licznikowi przebiegu samochodu.
        Zmiana zostanie odrzucona w przypadku próby cofnięcia licznika.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu!")

    def increment_odometer(self, miles):
        """Inkrementacja wartości licznika przebiegu samochodu o podaną wartość."""
        self.odometer_reading += miles
    
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


