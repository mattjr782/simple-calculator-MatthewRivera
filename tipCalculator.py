#used to determin if string can be float
def isNotFloat(string):
    try:
        float(string)
        return False
    except:
        return True

#ask for what was spent
cost = input("Enter the total cost: ")

while isNotFloat(cost):
    cost = input("That is not a number. Enter the total cost: ")

cost = round(float(cost), 2)

#ask for percent tipped
tipPercentage = input("What percentage do you want to tip: ")

while isNotFloat(tipPercentage):
    tipPercentage = input("That is not a number. enter the percent you want to tip: ")

tipPercentage = float(tipPercentage)

#calculate tip
tip = cost * tipPercentage/100
tip = round(tip, 2)

#calculate total
total = tip + cost
total = round(total, 2)

#print totals
print("Spent on meal ", cost)
print("tip percentage, ", tipPercentage)
print("total tip: tip", tip)
print("grand total: ", total)