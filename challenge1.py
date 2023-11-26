# Challenge 1: Converting 12-hour time to 24-hour time
# Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time 

def convert_to_24_hours(hour, minute, period):
    if minute < 10:
        minute = f"0{str(minute)}"

    if period ==  "am":
        if hour < 10:
            hour = f"0{str(hour)}"
        time = f"{str(hour)}{str(minute)}"
        return time
    else:
        if hour == 12:
            hour = "00"
        else:
            hour = hour + 12
        time = f"{str(hour)}{minute}"
        return time
    
