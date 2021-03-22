"""Andrea Cocco 2020
Chapter 5 Exercise 5-1 from the book:
    
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

The time module provides a function, also named time, that returns the current 
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. 
On UNIX systems, the epoch is 1 January 1970.

Write a script that reads the current time and converts it to a time of day in 
hours, minutes, and seconds, plus the number of days since the epoch.
"""

import time

secs_since_epoch = time.time()
mins_since_epoch = secs_since_epoch / 60 
hours_since_epoch = mins_since_epoch / 60
num_of_days = secs_since_epoch / 86400

print('Today is:', time.strftime("%d/%m/%Y", time.gmtime()))
print('Local time is:', time.strftime("%H:%M:%S", time.localtime()))
print('Epoch is:', time.strftime("%d/%m/%Y", time.gmtime(0)))
print('Seconds since the epoch (January 1, 1970):', int(secs_since_epoch))
print('Minutes since the epoch (January 1, 1970):', int(mins_since_epoch))
print('Hours since the epoch (January 1, 1970):', int(hours_since_epoch))
print('Days since the epoch (January 1, 1970):', int(num_of_days))
