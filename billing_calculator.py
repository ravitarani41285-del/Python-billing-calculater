print("Python Billing Calculator")
print("-------------------------")

customer_name = input("Customer name: ")
item_price = float(input("Item price: "))
quantity = int(input("Quantity: "))

total = item_price * quantity

print("-------------------------")
print("Customer:", customer_name)
print("Total Bill:", total)