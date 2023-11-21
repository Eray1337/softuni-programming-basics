# Входни размери на свободното пространство
width = int(input())
length = int(input())
height = int(input())

# Обем на свободното пространство
total_volume = width * length * height

# Въвеждане на брой кашони и пренос на багажа
while True:
    command = input()
    if command == "Done":
        break
    else:
        box_volume = int(command)
        total_volume -= box_volume
        if total_volume < 0:
            print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")
            break

if total_volume >= 0:
    print(f"{total_volume} Cubic meters left.")
