# Challenge 1: Converting 12-hour time to 24-hour time
# Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time 

# Define a function named convert_to_24_hours

def convert_12_hours_to_24_hours(hour, minute, period):
      #Checks if the minute is less than 10 and adds a zero if it's less than 10
    if minute < 10:
        minute = f"0{str(minute)}"
      #Checks if the period is at am
    if period ==  "am":
      #Checks if the hour is less than 10 and adds a zero if it's less than 10
        if hour < 10:
            hour = f"0{str(hour)}"
      # Combine the minute and hour into a string
        time = f"{str(hour)}{str(minute)}"
        return time
    else:
        # Set "00" for midnight if the hour is at 12
        if hour == 12:
            hour = "00"
        else:
           # Adds 12 to the hour when it clocks PM
            hour = hour + 12
            # Combines the hour and minute into a string and returns it
        time = f"{str(hour)}{minute}"
        return time
    
    
result = convert_12_hours_to_24_hours(4, 30, "pm")
print(result)