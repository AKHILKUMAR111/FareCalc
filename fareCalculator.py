from exception import WrongTypeError
fare_mapping={'Economy':10,'Premium':18,'SUV':25} #PER KM RATES FOR DIFFERENT TYPES OF RIDE

def surge_logic(total,hour):
    
    if hour>=17 and hour<=20:
        return 1.5*total
    else:
        return total
    
def calculate_fare(distance,ride_type,hour):
    if ride_type not in fare_mapping:
        raise WrongTypeError("This service is not available")
    total=distance*fare_mapping[ride_type]
    total=surge_logic(total,hour)
    return total
    
    
distance=int(input("Enter distance raveled: "))
ride_type=input("enetr the type of Ride: ")
hour=int(input("Enter the time of the  day in 24 hours formaat: "))
try:
    ride_estimate=calculate_fare(distance,ride_type,hour)
except WrongTypeError as e:
    print(f"Error: {e}")
else:
    print(f"ride charges: {ride_estimate} ")
