from datetime import datetime
from time import sleep

number_of_hours= int(input("Please enter number of hours: "))
number_of_minutes= int(input("Please enter number of minutes: "))
total_time= number_of_hours*3600 + number_of_minutes*60
for i in range(total_time):
    sleep(1)
    print('hi')