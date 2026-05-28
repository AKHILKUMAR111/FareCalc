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
    
    
if __name__ == '__main__':
    try:

        distance = int(input("Enter distance traveled: "))
        ride_type = input("Enter the type of Ride: ").strip()
        hour = int(input("Enter the time of day (24-hour format): "))
        
        ride_estimate = calculate_fare(distance, ride_type, hour)
        print(f"Ride charges: {ride_estimate}")
        
    except ValueError:
        print("Input Error: Distance and hours must be numeric values.")
    except WrongTypeError as e:
        print(f"Business Policy Exception: {e}")
