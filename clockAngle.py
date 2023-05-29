import numpy as np

def solve_clock_angle(time):
    '''
    Function to return the shortest angle between the hour and minute hand of an analog clock, 
    given the time in 24 hour HH:MM format
    
    Input: time in HH:MM format
    Output: angle in degrees
    '''
    
    ## split the time into hours and minutes
    hour, mins = [int(i) for i in time.split(":")]

    ## if the hour is greater than or equal to 12, subtract 12 
    if hour >= 12:
        hour -= 12
    ## get the angle of the hour hand
    hourAngle = hour * 30
    ## account for the fact that the hour hand moves throughout the hour
    ## first calculate the proportion of the hour that's passed
    mins_prop = mins/60
    ## now increment the hour hand 
    hourAngle += mins_prop * 30

    ## get the angle of the minute hand
    minsAngle = mins * 6

    ## calculate the difference between the angles
    angle = np.abs(hourAngle - minsAngle)
    ## calculate the shortest angle
    short_angle = min(angle, 360-angle)
    
    ## return result
    return short_angle

time = input("Enter time in HH:MM\n")
angle = solve_clock_angle(time)
print(f"The shortest angle between the hour and minute hand of an analog clock would be {angle} degrees")
