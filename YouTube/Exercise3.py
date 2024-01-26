w = float(input("Enter weight :"))

if w>0:
    choice = input("Choose kg(k) or lbs(l) :")
    if choice == 'k' :
        wt = w*2.20462
        print("Weight in lbs(pounds) : ",wt)
    elif choice == 'l':
        wt=w/2.20462
        print("Weight in kg : ",wt)
    else:
        print("Invalid choice")
else:
    print("Weight can not be lower than zero")

print("Program executed.")