# Write a function called your_vat that takes no parameters. The function asks
# the user to input the price of an item and VAT(%). The function should return
# the price of the item plus VAT. IF the price is 220, and VAT is 15%, it should
# return a vat inclusive price of 253. Make sure that the code can handle
# ValueError. Ensure the code runs until valid numbers are entered.
def your_vat() -> float:
    while True:
        try:
            price = float(input("Price of item: "))
            vat = float(input("VAT(%): "))
            return price + (price * (vat / 100))
        except ValueError:
            print("Please enter a valid item price.")

print(your_vat())