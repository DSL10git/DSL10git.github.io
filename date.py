from datetime import date

# Base info
birth_year = 2016  # Since age was 9 in 2025, birth year = 2025 - 9 = 2016
birth_month = 4
birth_day = 10

# Get today's date
today = date.today()

# Calculate age
age = today.year - birth_year

# Check if birthday hasn't occurred yet this year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

print(f"Current age: {age}")
