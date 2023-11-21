processor_price = float(input())
video_card_price = float(input())
ram_price = float(input())
ram_quantity = int(input())
discount_percentage = float(input())


processor_price_leva = processor_price * 1.57
video_card_price_leva = video_card_price * 1.57
ram_price_leva = ram_price * 1.57

total_price = (processor_price_leva + video_card_price_leva + (ram_price_leva * ram_quantity))

discount_amount = (processor_price_leva + video_card_price_leva) * discount_percentage

total_price_after_discount = total_price - discount_amount

print(f"Money needed - {total_price_after_discount:.2f} leva.")