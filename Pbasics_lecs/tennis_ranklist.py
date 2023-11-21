import math
number_of_tours = int(input())
starting_points = int(input())

points_gained = 0
wins_count = 0
for _ in range (number_of_tours):
    current_stage = input()

    if current_stage == "W":
        points_gained += 2000
        wins_count += 1
    elif current_stage == "F":
        points_gained += 1200
    elif current_stage == "SF":
        points_gained += 720

final_points = starting_points + points_gained
avg_points = points_gained / number_of_tours
percent_wins = wins_count / number_of_tours * 100

print(F"Final points: {final_points}")
print(f"Average points: {math.floor(avg_points)}")
print(f"{percent_wins:.2f}%")
