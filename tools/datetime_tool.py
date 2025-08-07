from datetime import datetime

def get_current_time():
    return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

def get_current_date():
    return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"
