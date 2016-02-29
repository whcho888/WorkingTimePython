# WorkingTimePython
You can check whether the day is working day or not super easily (including Korean Holidays). You can obtain various time or other day which based on your favor date. (Ex. Which month would be after 20days from now?)

# Availability
Any other foreign countries' working days can use this module, if you fix array of holidays on KoreanBDay class to your own countries holidays! (and change class name :) ).

# How to use (if today is "2016-2-29")
1. timeCalc.py
> from timeCalc import *  
> from datetime import datetime  
> get_month_of_next_monday(datetime.now())  
>\> 3  
> get_day_of_this_monday(datetime.now())  
>\> 29  

2. holidays.py
> from holidays import *  
> KBD.is_working_day(datetime.now())  
>\> True  
> KBD.is_working_day(datetime.now(), 1)  
>\> False  
> KBD.is_working_day(datetime.now(), -1)  
>\> False  
