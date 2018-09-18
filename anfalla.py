#Velja upphafsstaðsetningu x og y
locationx, locationy = 1, 1
#Setja inn færsluaðgerð, þe. setja inn skipanir fyrir færslu og láta kall færast
while locationx != 3 or locationy != 1:
    if (locationx ==1 and locationy == 1) or (locationx == 2 and locationy == 1):
        print("You can travel: (N)orth")
        locationchange = input("Direction: ")
        if locationchange.lower() == "n":
            locationy +=1
        else:
            print("Not a valid direction")
    elif locationx == 1 and locationy == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh")
        locationchange = input("Direction: ")
        if locationchange.lower() == "n":
            locationy +=1
        elif locationchange.lower() == "s":
            locationy -=1
        elif locationchange.lower() == "e":
            locationx +=1
        else:
            print("Not a valid direction")
    elif (locationx == 2 and locationy == 2) or (locationx ==3 and locationy == 3):
        print("You can travel: (W)est or (S)outh")
        locationchange = input("Direction: ")
        if locationchange.lower() == "s":
            locationy -=1
        elif locationchange.lower() == "w":
            locationx -=1
        else:
            print("Not a valid direction")
    elif locationx == 1 and locationy == 3:
        print("You can travel: (E)ast or (S)outh")
        locationchange = input("Direction: ")
        if locationchange.lower() == "s":
            locationy -=1
        elif locationchange.lower() == "e":
            locationx +=1
        else:
            print("Not a valid direction")
    elif locationx == 2 and locationy == 3:
        print("You can travel: (W)ast or (E)ast")
        locationchange = input("Direction: ")
        if locationchange.lower() == "w":
            locationx -=1
        elif locationchange.lower() == "e":
            locationx +=1
        else:
            print("Not a valid direction")
    elif locationx == 3 and locationy == 2:
        print("You can travel: (N)orth or (S)outh")
        locationchange = input("Direction: ")
        if locationchange.lower() == "s":
            locationy -=1
        elif locationchange.lower() == "n":
            locationy +=1
        else:
            print("Not a valid direction")
print("Victory")
#Setja inn færsluaðgerð, þe. setja inn skipanir fyrir færslu og láta kall færast
#Setja inn hvað gerjst gerist í hverjum af 9 tælum
#Setja inn rettar prent skipanir og biðji um input á réttum stöðum
#prenta út victory ef þetta lendir á réttum stað.
