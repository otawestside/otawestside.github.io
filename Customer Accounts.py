import sys
sys.version
print(Company Ledger)
customer_one = input("Name:") #customer data
print('Customer Name:', customer_one)
balance_one = float(input("Enter Current Balance:"))#account balance
print("Balance due the first of the month:", balance_one)
payment_made_one = float(input("Payment:"))#payment amount
print("Payment:", payment_made_one)
new_balance_one = balance_one - payment_made_one #new balance
print("Balance after payment:", new_balance_one)
extend_payment_one = input("Extend due date extra 15 days for $10 fee?")
extended_payment_balance = new_balance_one + 10
if extend_payment_one =="yes":
    print("Would you like to extend any balance due an extra 15 days for a $10 fee?", extend_payment_one)
    print("Balance due by the 15th:", extended_payment_balance )
else:
    print("Would you like to extend any balance due an extra 15 days for a $10 fee?", extend_payment_one)
    print("Balance due the first of the month:", new_balance_one)
print("Thank You!")
print()
customer_two = input("Name:")
print('Customer Name:', customer_two)
balance_two = float(input("Enter Current Balance:"))
print("Balance due the first of the month:", balance_two)
payment_made_two = float(input("Payment:"))
print("Payment:", payment_made_two)
new_balance_two = balance_two - payment_made_two
print("Balance after payment:", new_balance_two)
extend_payment_two = input("Extend due date extra 15 days for $10 fee?")
if extend_payment_two =="yes":
    print("Would you like to extend any balance due an extra 15 days for a $10 fee?", extend_payment_two)
    print("Balance due by the 15th:", extended_balance_two)
else:
    print("Would you like to extend any balance due an extra 15 days for a $10 fee?", extend_payment_two)
    print("Balance due the first of the month:", new_balance_two)
print("Thank You!")
print()
print("Summary of Receivables:")
print("Receivables by the 1st of the month:", new_balance_two)
print("Receivables by the 15th of the month:", extended_payment_balance)

