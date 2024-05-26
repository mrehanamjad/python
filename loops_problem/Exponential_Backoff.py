# Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1 # in seconds
max_retries = 5
attamps = 0

while attamps < max_retries:
    print("Attemp",attamps + 1 , "-wait time",wait_time, "seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attamps += 1
