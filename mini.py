menu ={
    "Gobi" :50,
    "Pani puri":30,
    "Masala puri": 35,
    "Egg fried rice": 50,
    "Veg fried rice": 40,
    "Coffee": 20,
    "Tea": 15
}
print("WELCOME TO OUR CAFE!!!")
print("MENU")
print("Gobi: Rs 50\nPani puri: Rs 30\nMasala puri: Rs 35\nEgg fried rice: Rs 50\nVeg fried rice: Rs 40\nCoffee: Rs 20\nTea: 15\n")

ORDER_TOTAL=0

item1=input("Enter the item name you wanted to order : ")
if item1 in menu:
    ORDER_TOTAL+=menu[item1]
    print(f"Your item {item1} has been added to your order")

else:
    print("SORRY!!!")
    print(f"Ordered item {item1} is not available in our menu") 

another=input("Would you like to order some more?(Yes/No):")   
if another=="yes".lower():
    item2=input("Enter second item :")
    if item2 in menu:
        ORDER_TOTAL+=menu[item2]
        print(f"Your item {item2} has been added to your order")
    else: 
        print("SORRY!!!")
        print(f"Ordered item {item1} is not available in our menu") 
print(f"Total amount to be paid is Rs {ORDER_TOTAL}")



        