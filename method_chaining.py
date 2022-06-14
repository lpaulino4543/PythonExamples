class Car:
    def turn_on(self):
        print("You've turned on your engine")
        return self

    def drive(self):
        print("You're currently driving")
        return self

    def brake(self):
        print("You stepped on the brakes")
        return self
    def turn_off(self):
        print("You've turned off your engine")
        return self
car = Car()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
