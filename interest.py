principal; int = 1000        # Principal amount (initial investment)
rate: float = 0.05           # Annaul interest rate (the rate at which the extra money that is paid back when principal is borrowed)
numyears: int = 5            # Number of compounding periods per year (to pay or charge interest on an amount that includes any interest already earned or charged)
year: int = 1                # Time in years
while year <= numyears:
    principal = principal * (1 + rate)  # Interest is compounded once per year
    print (year, principal)
    year += 1
