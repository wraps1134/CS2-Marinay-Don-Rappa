# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ").strip()

if name == "":
    print("Customer name is required.")
    name = input("Enter customer name: ")
else:
    print("")

try:
    previous =float(input("Enter previous meter reading: "))
    if previous > -1:
        print("")
    else:
        print("Value must be at least 0")
        previous =float(input("Enter previous meter reading: "))
except ValueError:
    print("Enter a valid value")
    previous =float(input("Enter previous meter reading: "))

try:
    current = float(input("Enter current meter reading: "))
    if current >= previous:
        print("")
    else:
        print("Number must be at least the previous reading")
        current = float(input("Enter current meter reading: "))
except ValueError:
    print("Enter a valid value")
    current = float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
