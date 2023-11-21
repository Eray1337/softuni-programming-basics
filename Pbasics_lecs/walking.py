steps_count = 0
steps_goal = 10000

while steps_count < steps_goal:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        steps_count += steps_to_home
        break
    else:
        walked_steps = int(command)
        steps_count += walked_steps

if steps_count >= steps_goal:
    print(f'Goal reached! Good job!')
    print(f'{steps_count - steps_goal} steps over the goal!')
else:
    print(f'{steps_goal - steps_count} more steps to reach goal.')