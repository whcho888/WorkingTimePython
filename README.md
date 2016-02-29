# WorkingTimePython
You can check easily whether the day is working day or not (including Holidays).   
You can also obtain various time or other day which based on your favor date. (Ex. Which month would be after 20days from now?)

# Availability
Any other foreign countries' working days can use this module, if you fix array of holidays on KoreanBDay class to your own countries holidays! [and change class name :)].
This module has been tested only on python 2.7.

# How to use (if today is "2016, 2, 29")
1. workingDays.py
> from holidays import *  
KBD.is_working_day(datetime.now())  
\> True  
KBD.is_working_day(datetime.now(), 1)  
\> False  
KBD.is_working_day(datetime.now(), -1)  
\> False  
KBD.get_before_workingDate(datetime.now(), 3)  
\> datetime.date(2016, 2, 26)  
KBD.get_xday_before_workingDate(datetime.now(), 3)  
\> datetime.date(2016, 2, 24)  


2. timeCalc.py
> from timeCalc import *  
from datetime import datetime  
get_month_of_next_monday(datetime.now())  
\> 3  
get_day_of_this_monday(datetime.now())  
\> 29  
