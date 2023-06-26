
class RideManager:
    def __init__(self,name) -> None:
        print('Ride Manager Activated')
        self.name=name
        self.__availableCars=[]
        self.__availableBikes=[]
        self.__availableCngs=[]
        self.__trip_history=[]
        self.__income=0
    
    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type=='car':
            self.__availableCars.append(vehicle)
        elif vehicle_type=='bike':
            self.__availableBikes.append(vehicle)
        else:
            self.__availableCngs.append(vehicle)

    def get_availableCars(self):
        return self.__availableCars
    
    def get_income(self):
        return self.__income
    
    def trip_history(self):
        return self.__trip_history

    def find_a_match(self, rider, vehicle_type, destination):
        vehicles=None
        if vehicle_type=='car':
            vehicles=self.__availableCars
        elif vehicle_type=='bike':
            vehicles=self.__availableBikes
        else:
            vehicles=self.__availableCngs

        if len(vehicles) == 0:
            print(f'Sorry! No {vehicle_type} available now')
            return False
        for vehicle in vehicles:
            
            if abs(rider.location - vehicle.driver.location) < 10:
                distance=abs(rider.location-destination)
                fare=distance * vehicle.rate
                if fare > rider.balance:
                    print('You do not have sufficient balance', fare, rider.balance)
                    return False
                
                if vehicle.status=='available':
                    trip_info=f'Match {vehicle.vehicle_type} {rider.name} with driver {vehicle.driver.name} with ride fare: {fare}, driver fare:{fare*0.8} from {rider.location} to {destination}'
                    print(trip_info)
                    self.__trip_history.append(trip_info)
                    rider.start_trip(fare, trip_info)
                    # print("Available vehicles", len(vehicles))
                    vehicle.status='unavailable'
                    vehicles.remove(vehicle)
                    vehicle.driver.start_trip(rider.location, destination, fare * 0.8, trip_info)
                    self.__income += fare * 0.2
                    # print("Available vehicles", len(vehicles))
                    # print('Potential', rider.location, vehicle.driver.location)
                    # print('Found a match for you')
                    # print('=======')
                    return True
                   
uber=RideManager('Uber')
