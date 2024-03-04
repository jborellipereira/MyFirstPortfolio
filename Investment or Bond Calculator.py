import math

print("\nWelcome to the Investment or Bond Calculator.\n")

investment_or_bond = input(str('''To calculate the amount of interest you'll earn on an investment please enter 'Investment'.
To calculate the amount you'll have to pay on a home loan please enter 'Bond':\n''')).casefold()

if investment_or_bond  == "investment":
        P = float(input("How much are you depositing?\n£"))
        r = float(input("At which interest rate percentage?\n"))
        r = (r/100)
        t = float(input("How many years are you planning to invest for?\n"))
        simp_comp = str(input("Choose 'Simple' or 'Compound' interest.\n")).casefold()
        
        if simp_comp == "simple":
            simp_comp = P*(1 + r * t)
            interest = simp_comp
            print(f"The interest earned over {t} years will be £{interest:}")
        else:
            simp_comp = P*math.pow((1+r),t)
            interest = simp_comp
            print(f"Your interest earned over {t} years will be £{interest:}")

elif investment_or_bond == "bond":
        P = float(input("What is the current value of the house?\n£"))
        i = float(input("At which interest rate percentage?\n"))
        i = ((i/100)/12)
        n = float(input("For how many months do you wish to repay?\n"))
        repayment = (i*P)/(1 -(1+i)**(-n)) 
        print(f"Your monthly repayment will be £{repayment:}")

else:
    print("Error: Invalid input.")