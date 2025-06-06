#Hello, this is a mortgage/budget calculator

# monthlyIncome=float(input("Please enter your estimated monthly revenue after taxes: ")) 

# rent=float(input("Please enter rent and estimated utility costs per month: "))

# utilities=float(input("Please enter monthly cost of utilities: "))

#recurringMonthlyCosts=float(input("Please enter recurring monthly costs: ")) 

# random=float(input("Any miscellaneous costs"))

def mortgageCalculator():
  
  # Cost of Home
  homeCost=int(input("Home Price: ")) 

  # Percentage of downpayment
  downPaymentPercentage = int(input("Downpayment percentage: "))/100

  # Downpayment
  downPayment = homeCost*downPaymentPercentage

  # Loan amount
  principalPayment = homeCost - downPayment
  
  #interest rate **On average, places like Toronto may be higher**
  rate=float(input("Interest rate: " ))/100
  
  # months in a year to pay
  n=12 
  
  # years of terms
  t=int(input("Length of term (years): ")) 
  
  ratePerMonth=rate/n
  totalMonthsInTerm=-n*t
  
  numerator=principalPayment*ratePerMonth
  denominator=((1-(1+ratePerMonth) ** (totalMonthsInTerm)))
  
  return round(numerator / denominator,2)

print("Option: ${0} per month".format(mortgageCalculator()))

''' 
def budgetCalculator():
  monthlyIncome=float(input("Please enter your estimated monthly revenue after taxes: "))

  rent=float(input("Rent and or mortgage: "))

  utilities=float(input("Utility costs: "))

  recurringCosts=float(input("Recurring monthly costs: "))

  random=float(input("Any miscellaneous costs: "))

  monthlyCosts = rent+utilities+recurringCosts+random 
  
  monthlyRevenue = float(monthlyIncome - monthlyCosts)
  
  return monthlyRevenue

print("Monthly revenue: ${0}".format(budgetCalculator()))  


LIST FOR SELF:
  * OOP??
    * FUNCTIONS
    * CONDITIONALS
    * LIST/DICTIONARIES
    * CLASSES 

  * ML
    * SUPERVISED VS UNSUPERVISED
      * REGRESSION VS CLASSIFICATIONS (BINARY VS MULT) -> CLUSTERS?
    * REINFORCED 
    * GEN AI

  * DEFINITIONS:
    * AI , ML, DL 

def eatMeals():
  print("eat breakfast")
  print("eat lunch")
  print("eat dinner")
  
for days in range(0,7):
  eatMeals()

'''