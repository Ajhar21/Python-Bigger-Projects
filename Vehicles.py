from abc import ABC, abstractclassmethod
from time import sleep
class Vehicle(ABC):
    speed={
        'car': 30,
        'bike': 50,
        'cng': 15
    }
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        self.vehicle_type=vehicle_type
        self.license_plate=license_plate
        self.status='available'
        self.rate=rate
        self.driver=driver
        self.speed=Vehicle.speed[vehicle_type]

    @abstractclassmethod
    def start_driving(self):
        pass

    @abstractclassmethod
    def trip_finished(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
    
    def start_driving(self,start, destination):
        self.status='unavailable'
        print(self.vehicle_type, self.license_plate, 'Started trip')
        distance=abs(destination-start)

        for i in range(distance):
            sleep(0.1)
            print(f'Driving {self.vehicle_type} {self.license_plate} position: {i} of distance: {distance}\n')
        self.trip_finished()

    def trip_finished(self):
        print(self.vehicle_type, self.license_plate, 'Finished trip')
        self.status='available'
        
class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
    
    def start_driving(self,start, destination):
        self.status='unavailable'
        print(self.vehicle_type, self.license_plate, 'Started trip')
        distance=abs(destination-start)

        for i in range(distance):
            sleep(0.1)
            print(f'Driving {self.vehicle_type} {self.license_plate} position: {i} of distance: {distance}\n')
        self.trip_finished()

    def trip_finished(self):
        print(self.vehicle_type, self.license_plate, 'Finished trip')
        self.status='available'
        
class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
    
    def start_driving(self,start, destination):
        self.status='unavailable'
        print(self.vehicle_type, self.license_plate, 'Started trip')
        distance=abs(destination-start)

        for i in range(distance):
            sleep(0.1)
            print(f'Driving  {self.vehicle_type} {self.license_plate} position: {i} of distance: {distance}\n')
        self.trip_finished()

    def trip_finished(self):
        print(self.vehicle_type, self.license_plate, 'Finished trip')
        self.status='available'



       

