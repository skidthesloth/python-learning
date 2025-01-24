principal = 1000        # Principal amount (initial investment)
rate = 0.05             # Annaul interest rate (as a decimal)
numyears = 5            # Number of compounding periods per year
year = 1                # Time in years
while year <= numyears:
    principal = principal * (1 + rate)  # Interest is compounded once per year
    print (year, principal)
    year += 1
    