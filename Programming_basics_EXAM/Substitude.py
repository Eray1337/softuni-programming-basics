# Input
k = int(input())
l = int(input())
m = int(input())
n = int(input())

substitute_count = 0

for first_digit_k in range(k, 9):
    for second_digit_l in range(9, l - 1, -1):
        for first_digit_m in range(m, 9):
            for second_digit_n in range(9, n - 1, -1):
                if first_digit_k % 2 == 0 and second_digit_l % 2 != 0 and first_digit_m % 2 == 0 and second_digit_n % 2 != 0:
                    if first_digit_k != first_digit_m or second_digit_l != second_digit_n:
                        print(f"{first_digit_k}{second_digit_l} - {first_digit_m}{second_digit_n}")
                        substitute_count += 1
                        if substitute_count == 6:
                            break
                    else:
                        print("Cannot change the same player.")
            if substitute_count == 6:
                break
        if substitute_count == 6:
            break
    if substitute_count == 6:
        break
