from datetime import datetime
from time import sleep
import os


number_of_hours= int(input("Please enter number of hours: "))
number_of_minutes= float(input("Please enter number of minutes: "))
total_time= number_of_hours*3600 + number_of_minutes*60
time_current=total_time
while 0 < time_current:
    sleep(1)
    time_current-=1
else: os.system("/Users/ohmpanchal/HackED Beta/Pawggers/Dog Classifier'/PawMailer/PawMailer/Program.cs")
