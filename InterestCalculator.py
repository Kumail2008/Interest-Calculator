print("Welcome to interest calculator...\n\nWhat would you like to calculate?\n")
print("[1] Simple interest\n[2] Compound interest")
option = int(input(""))

if option == 1:
    print("\nSimple Interest Calculator...\n")
    p = float(input("What is the initial balance?\n"))
    interestRate = float(input("What is the annual interest rate?\n"))
    t = float(input("How many years would you like to calculate for?\n"))
    r = float(interestRate/100)
    amount = p*(1+r*t)
    interestEarned = float(amount - p)
    a = '{:,.2f}'.format(amount)
    ie = '{:,.2f}'.format(interestEarned)

    print("Your new balance would be...\n")
    print("$"+a)
    print("Interest Earned: $"+ie)

elif option == 2:
    print("\nCompound Interest Calculator...\n")
    p = float(input("What is the initial balance?\n"))
    interestRate = float(input("What is the interest rate?\n"))
    t = float(input("How many years would you like to calculate for?\n"))
    n = float(input("How many times is interest applied during this time period?\n"))
    r = float(interestRate/100)
    amount = p*(1+r/n)**(t*n)
    interestEarned = float(amount - p)
    a = '{:,.2f}'.format(amount)
    ie = '{:,.2f}'.format(interestEarned)

    print("Your new balance would be...\n")
    print("$"+a)
    print("Interest Earned: $"+ie)

