# Create project countdown timer 
import time

# make function for countdown:
def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds , 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs) # 00:59
        print(time_format, end='\r') #end for in singleline count
        time.sleep(1)  # delay
        seconds -=1
    print("00:00 \n Time's Up!")

# input for totalseconds to count:
time_seconds = int(input("Enter seconds to count:"))

countdown_timer(time_seconds)