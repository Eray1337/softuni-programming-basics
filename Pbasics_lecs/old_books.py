book_searching = input()
book_count = 0
current_book = input()

is_book_found = False
while current_book != "No More Books":
    if current_book == book_searching:
        is_book_found = True
        print(f"You checked {book_count} books and found it.")
        break
    else:
        book_count += 1
        current_book = input()
if not is_book_found:
    print('The book you search is not here!')
    print(f"You checked {book_count} books.")