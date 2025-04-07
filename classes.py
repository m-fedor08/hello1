class Flight():
    def __init__(self, capaciti):
        self.capaciti = capaciti
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capaciti - len(self.passengers)
    
flight = Flight(3)

people = ["Harry", "Ron", "Hermiona", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")

