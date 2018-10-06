pielist = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
print("Welcome to the House of Pies! Here are our pies:")

for pie in pielist:
    print("[" + str(pielist.index(pie)) + "]" + pie)

piecart = []
new = "Y" 
while new =="Y":
    selected = input("Select a pie by number")
    piecart.append(pielist[int(selected)])
    print("Great! We'll have that " + pielist[int(selected)] + " Pie right out for you.")
    new = input("Would you like to order another pie?")
    
#print(piecart)
print("You have purchased " + str(len(piecart)) + " pies.")






