#Hello, this is a mortgage/budget calculator

def mortgageCalculator():
  
  # Cost of Home
  homeCost =int(input("Please enter home Price: ")) 

  # Percentage of downpayment
  downPaymentPercentage = int(input("Please enter the percentage of downpayment expected: "))/100

  # Downpayment
  downPayment = homeCost * downPaymentPercentage

  # Loan amount
  principalPayment = homeCost - downPayment
  
  #interest rate **On average; places like Toronto may be higher**
  rate = float(input("Please enter the interest rate: " ))/100
  
  # months in a year to pay
  n = 12 
  
  # years of terms
  t = int(input("Please enter the length of term, in years: ")) 
  
  ratePerMonth = rate / n
  totalMonthsInTerm = -n * t
  
  numerator = principalPayment * ratePerMonth
  denominator = ((1- (1 + ratePerMonth) ** (totalMonthsInTerm)))
  
  return round(numerator / denominator,2)

print("Option: ${0} per month".format(mortgageCalculator()))

