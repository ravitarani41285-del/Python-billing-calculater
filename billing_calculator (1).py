print("=== PYTHON BILLING CALCULATOR ===")

customer_name = input("Enter customer name: ")

item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = item_price * quantity

print("\n========== BILL ==========")
print("Customer:", customer_name)
print("Item:", item_name)
print("Price:", item_price)
print("Quantity:", quantity)
print("Total Bill:", total)
print("==========================")