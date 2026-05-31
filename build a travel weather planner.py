# 1. Create the variables with sample test values
distance_mi = 5           # A number representing distance
is_raining = False        # A boolean (True or False)
has_bike = True           # A boolean (True or False)
has_car = False           # A boolean (True or False)
has_ride_share_app = True # A boolean (True or False)

# 2. Evaluate the conditions in ascending order using conditional statements
if not distance_mi:
    # Condition 4: If distance_mi is a falsy value (like 0)
    print(False)

elif distance_mi <= 1:
    # Condition 5: Distance is less than or equal to 1 mile
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi <= 6:
    # Condition 6: Distance is greater than 1 mile and less than or equal to 6 miles
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

else:
    # Condition 7: Distance is greater than 6 miles
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
