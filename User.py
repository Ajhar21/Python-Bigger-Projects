import hashlib
from random import randint, choice
from License_Authority import BRTA
from Vehicles  import Car, Bike, Cng
from Ride_Manager import uber
import threading
license_authority=BRTA()

class UserExistAlready(Exception):
    def __init__(self, email,*args: object) -> None:
        print(f'{email} already exist by exception')
        super().__init__(*args)

class User:
    def __init__(self, name, email, password) -> None:
        self.name=name
        self.email=email
        self.password=password
        self.hashed_pass= hashlib.md5(password.encode()).hexdigest()

        is_user_exist=False
        first_check_file=True

        if first_check_file is False:
            with open('user.txt', 'r') as file:
                if email in file.read():
                    # print(f'{email} already exist')
                    # raise UserExistAlready(email)
                    is_user_exist=True
            file.close()
        
        if is_user_exist==False:
            with open('user.txt', 'a') as file:
                file.write(f'{email} {self.hashed_pass}\n')
            file.close()
            first_check_file=False
        # print('User Created Succesfully')
    
    @staticmethod
    def log_in(email, password):
        with open ('user.txt', 'r') as file:
            lines= file.readlines()
        stored_pass =''
        for line in lines:
            if email in line:
                print('Email Found')
                stored_pass= line.split(' ')[1]
        
        hashed_log_pass= hashlib.md5(password.encode()).hexdigest()
        if hashed_log_pass==stored_pass:
            print('Valid User')
            return True
        else:
            print('Invalid User')
            return False
    
class Rider(User):
    def __init__(self, name, email, password, location, balance):
        super().__init__(name, email, password)
        self.location=location
        self.balance=balance
        self.__trip_history=[]
    
    def set_location(self, location):
        self.location=location
    
    def get_location(self):
        return self.location
    
    def request_trip(self, destination):
        # self.destination=destination
        pass

    def start_trip(self, fare, trip_info):
        print(f'A trip started for {self.name}')
        self.balance -=fare
        self.__trip_history.append(trip_info)

    def get_trip_history(self):
        return self.__trip_history

class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        self.location=location
        self.license=license
        self.__trip_history=[]
        self.valid_driver=license_authority.validate_license(self.email, self.license)
        self.earning=0
        self.vehicle=None
    
    def take_driving_test(self):
        result=license_authority.take_driving_test(self.email)
        if result==False:
            # print('Sorry, you have failed')
            self.license=None
        else :
            # print('You have passed')
            self.license=result
            self.valid_driver=True

    def register_a_vehicle(self, vehicle_type, rate):
        if self.valid_driver is True:
            if vehicle_type=='car':
                self.vehicle=Car(vehicle_type, self.license, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            elif vehicle_type=='bike':
                self.vehicle=Bike(vehicle_type, self.license, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            else:
                self.vehicle=Cng(vehicle_type, self.license, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
        else:
            pass
            # print('You are not a valid driver!')

    def start_trip(self,start, destination, fare, trip_info):
        self.earning += fare
        self.location=destination
        self.__trip_history.append(trip_info)
        trip_thread=threading.Thread(target=self.vehicle.start_driving, args=(start, destination,))
        trip_thread.start()
        # trip_thread.join() # will work manually again
        # self.vehicle.start_driving(start, destination) # No need to call function manually when it threading
    
    def get_trip_history(self):
        return self.__trip_history

rider1=Rider('rider1', 'rider1@gmail.com', 'rider1', randint(0,30),1000)
# print(dir(rider1))
rider2=Rider('rider2', 'rider2@gmail.com', 'rider2', randint(0,30),5000)
rider3=Rider('rider3', 'rider3@gmail.com', 'rider3', randint(0,30),5000)

vehicle_list=['car', 'bike', 'cng']

for i in range(1,100):
    driver=Driver(f'driver{i}', f'driver{i}@gmail.com', f'driver{i}', randint(1,100), randint(1000,9999))
    driver.take_driving_test()
    driver.register_a_vehicle(choice(vehicle_list), 10)

# print(uber.get_availableCars())

uber.find_a_match(rider1, choice(vehicle_list), randint(1,100))
uber.find_a_match(rider2, choice(vehicle_list), randint(1,100))
uber.find_a_match(rider3, choice(vehicle_list), randint(1,100))
uber.find_a_match(rider1, choice(vehicle_list), randint(1,100))
uber.find_a_match(rider2, choice(vehicle_list), randint(1,100))
uber.find_a_match(rider1, choice(vehicle_list), randint(1,100))

print(f'{uber.name} Income Is: ',uber.get_income())
print(uber.trip_history())

