# ===========================
# Home Work --- 11
# Home Work of Functions
# Art Supplies Billing Tool
# ===========================

# Part 1:
def greet_customer():
    print("Welcome to art supplies store.")
    print("Best art supplies available.")
    
# Part 2:
greet_customer()

# Part 3:
price_per_art_material = float(input("Enter the price per art material: "))
art_material_sold = int(input("Enter the number of art material sold: "))

# Part 4:
def calculate_total(price,art_material):
    total = price * art_material
    return total

# Part 5:
total_cost = calculate_total(price_per_art_material,art_material_sold)
 
# Part 6:
rounded_total = round(total_cost,2)
print("Total Cost   :",rounded_total)

# Part 7:
amount_paid = float(input("Enter the amount paid by the user: "))

# Part 8:
def calculate_change(paid,total):
    change = paid - total
    return change

# Part 9:
change_due = calculate_change(amount_paid,rounded_total)
rounded_change = round(change_due,2)

# Part 10:
def thank_you_message(art_materials):
    if art_materials >= 5:
        return "Wow Big Order! Thank you so much for your support."
    
    else:
        return "Thank you for standing by the store."

# Part 11:  
closing_message = thank_you_message(art_material_sold)

# Part 12:
print("")
print(" ===== ART SUPPLIES STORE RECEIPT ===== ")   
print("Price per art material     :",price_per_art_material) 
print("Art material sold          :",art_material_sold)
print("Total cost                 :",rounded_total)
print("Amount paid                :",amount_paid)
print("Change due                 :",change_due)
print(closing_message)
print("==========================================")