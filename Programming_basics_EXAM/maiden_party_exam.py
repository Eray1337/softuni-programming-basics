#Михаела държи сама да организира и заплати моминското си парти. Тя планува плащането да стане с
#приходите от онлайн магазина й. Да се напише програма, която пресмята печалбата от продажбите й.
#Цени на различните артикули:
# Любовно послание - 0.60 лв.
# Восъчна роза - 7.20 лв.
# Ключодържател - 3.60 лв.
# Карикатура - 18.20 лв.
# Късмет изненада - 22 лв.
#Ако поръчаните артикули са 25 или повече магазинът прави отстъпка 35% от общата цена. От спечелените
#пари Михаела трябва да предвиди и 10% разход за хостинг. Да се пресметне дали парите ще й стигнат да си
#плати моминското парти.

party_price = float(input())
count_love_letters = int(input())
count_wax_roses = int(input())
count_keychains = int(input())
count_caricatures = int(input())
count_fortunes = int(input())

total_price = count_love_letters * 0.60 + count_wax_roses * 7.20 + count_keychains * 3.60 + count_caricatures * 18.20 + count_fortunes * 22

items_count = count_love_letters + count_wax_roses + count_keychains + count_caricatures + count_fortunes
discount = 0

if items_count >= 25:
    discount = total_price * 0.35

final_price = total_price - discount

hosting = final_price * 0.10
income = final_price - hosting
if income >= party_price:
    print(f"Yes! {income - party_price:.2f} lv left.")
else:
    print(f"Not enough money! {party_price - income:.2f} lv needed.")


