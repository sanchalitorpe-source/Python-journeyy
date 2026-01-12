from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Now:", now)

# Format date
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))

# Date arithmetic
today = datetime.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print("Yesterday:", yesterday.date())
print("Tomorrow:", tomorrow.date())

# Parse string to date
date_str = "2026-01-14"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed Date:", parsed_date.date())
