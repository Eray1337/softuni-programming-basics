needed_money = float(input())
available_money = float(input())
days_counter = 0
spending_counter = 0

while available_money < needed_money and spending_counter < 5:
    command = input()

    if command == 'save':
        money = float(input())
        days_counter += 1
        available_money += money
        spending_counter = 0
    elif command == 'spend':
        money = float(input())
        days_counter += 1
        available_money -= money
        spending_counter += 1
    if available_money < 0:
        available_money = 0

if spending_counter == 5:
    print(f"You can't save the money.")
    print(f"{days_counter}")
elif available_money >= needed_money:
    print(f"You saved the money for {days_counter} days.")
