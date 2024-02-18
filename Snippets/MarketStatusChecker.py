import pytz
import datetime

# Market holidays
holidays = [
    "01-01",
    "01-15",
    "02-19",
    "03-29",
    "05-27",
    "06-19",
    "07-04",
    "09-02",
    "11-28",
    "12-25",
]

def is_market_open():
    # Set the timezone to US Eastern Time (ET)
    tz = pytz.timezone('America/New_York')
    now = datetime.datetime.now(tz)

    # Get date in month-day format
    short_date = datetime.date.today().strftime("%m-%d")

    # Check if it's a weekday (Monday to Friday) and within trading hours
    return 0 <= now.weekday() <= 4 and 9 * 60 + 30 <= now.hour * 60 + now.minute <= 16 * 60 and not short_date in holidays

# Example usage
if is_market_open():
    print("The US stock market is currently open.")
else:
    print("The US stock market is currently closed.")
