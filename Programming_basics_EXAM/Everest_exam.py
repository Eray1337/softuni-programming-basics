current_height = 5364  # Starting height
days = 1  # Starting day

while current_height < 8848:
    command = input()
    if command == "END":
        break
    meters_climbed = int(input())

    if command == "Yes":
        days += 1
        if days > 5:
            break

    current_height += meters_climbed

    if current_height >= 8848:
        break

if current_height >= 8848:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(f"{current_height}")
