# Input
dancers = int(input())
points = float(input())
season = input()
place = input()

# Calculate the money earned
if place == "Bulgaria":
    money = dancers * points
else:
    money = dancers * points * 1.5

# Calculate expenses
if place == "Bulgaria":
    if season == "summer":
        money *= 0.95
    else:
        money *= 0.92
else:
    if season == "summer":
        money *= 0.90
    else:
        money *= 0.85

# Calculate charity and money per dancer
charity = money * 0.75
money_per_dancer = (money - charity) / dancers

# Output
print("Charity - {:.2f}".format(charity))
print("Money per dancer - {:.2f}".format(money_per_dancer))