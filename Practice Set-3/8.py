# 8. An online selling app wants to develop a application to calculate shipping charges on the
# purchase. Accept amount from the user and calculate the shipping charges.
# The shipping charges are as below:
# Shopping amount less than 1500 – The shipping charges is Rs. 100/-
# --Type the message: Please purchase (1500-amount) to avail shipping charge of Rs. 80/-
# --Please pay (amount+100)
# Shopping amount more than 1500 and less than 3000 – The shipping charges is Rs. 70/-
# --Type the message: Please purchase (3000-amount) to avail shipping charge of Rs. 50/-
# --Please pay (amount+70)
# Shopping amount more than 3000 – Free shipping + 7% discount on amount
# --Type a message: You saved (amount*7/100)
# --Please pay (amount – discount)

purchase_amount = float(input("Enter the purchase amount: "))
slab_1_limit = 1500
slab_2_limit = 3000
if purchase_amount < slab_1_limit:
    shipping_charge = 100
    discount_message = (f"Please purchase {slab_1_limit - purchase_amount} to avail shipping charge of Rs. 80/-")
elif purchase_amount < slab_2_limit:
    shipping_charge = 70
    discount_message = (f"Please purchase {slab_2_limit - purchase_amount} to avail shipping charge of Rs. 50/-")
else:
    shipping_charge = 0
    discount_percentage = 0.07
    discount_message = (f"You saved {purchase_amount * discount_percentage} on shipping!")
    purchase_amount -= purchase_amount * discount_percentage
print(f"Shipping Charges: Rs. {shipping_charge}/-")
print(discount_message)
print(f"Please pay: Rs. {purchase_amount + shipping_charge}/-")

#output:=
Enter the purchase amount: 800
Shipping Charges: Rs. 100/-
Please purchase 700.0 to avail shipping charge of Rs. 80/-
Please pay: Rs. 900.0/-