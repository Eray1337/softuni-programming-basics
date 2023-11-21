# Input number of computers
n = int(input())

# Initialize variables
total_sales = 0
total_ratings = 0

# Processing each computer's data
for _ in range(n):
    data = int(input())
    rating = data % 10
    possible_sales = data // 10

    # Determine actual sales based on rating
    if rating == 2:
        actual_sales = 0
    elif rating == 3:
        actual_sales = 0.50 * possible_sales
    elif rating == 4:
        actual_sales = 0.70 * possible_sales
    elif rating == 5:
        actual_sales = 0.85 * possible_sales
    elif rating == 6:
        actual_sales = possible_sales

    # Add to totals
    total_sales += actual_sales
    total_ratings += rating

# Calculate average rating
average_rating = total_ratings / n

# Print results
print(f"{total_sales:.2f}")
print(f"{average_rating:.2f}")
