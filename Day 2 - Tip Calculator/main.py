print("Welcome to tip calculator!")
total_amt = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 o4 15? "))
percent = tip/100
multiply = percent * total_amt
final_amount = multiply + total_amt
split = int(input("How many people to split the bill? "))
final_answer = round(final_amount/split, 2)
print(f"Each person should pay: $ ${final_answer}.")