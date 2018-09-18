#Velja upphafsstaðsetningu x og y
locationx, locationy = 1, 1
#Setja inn færsluaðgerð, þe. setja inn skipanir fyrir færslu og láta kall færast
#Setja inn færsluaðgerð, þe. setja inn skipanir fyrir færslu og láta kall færast
#Setja inn hvað gerjst gerist í hverjum af 9 tælum
#Setja inn rettar prent skipanir og biðji um input á réttum stöðum
while locationx != 3 or locationy != 1:
    if (locationx ==1 and locationy == 1) or (locationx == 2 and locationy == 1):
        print("You can travel: (N)orth.")
        while (locationx ==1 and locationy == 1) or (locationx == 2 and locationy == 1):
            locationchange = input("Direction: ")
            if locationchange.lower() == "n":
                locationy +=1
            else:
                print("Not a valid direction!")
    elif locationx == 1 and locationy == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        while locationx == 1 and locationy == 2:
            locationchange = input("Direction: ")
            if locationchange.lower() == "n":
                locationy +=1
            elif locationchange.lower() == "s":
                locationy -=1
            elif locationchange.lower() == "e":
                locationx +=1
            else:
                print("Not a valid direction!")
    elif (locationx == 2 and locationy == 2) or (locationx ==3 and locationy == 3):
        print("You can travel: (S)outh or (W)est.")
        while (locationx == 2 and locationy == 2) or (locationx ==3 and locationy == 3):
            locationchange = input("Direction: ")
            if locationchange.lower() == "s":
                locationy -=1
            elif locationchange.lower() == "w":
                locationx -=1
            else:
                print("Not a valid direction!")
    elif locationx == 1 and locationy == 3:
        print("You can travel: (E)ast or (S)outh.")
        while locationx == 1 and locationy == 3:
            locationchange = input("Direction: ")
            if locationchange.lower() == "s":
                locationy -=1
            elif locationchange.lower() == "e":
                locationx +=1
            else:
                print("Not a valid direction!")
    elif locationx == 2 and locationy == 3:
        print("You can travel: (E)ast or (W)est.")
        while locationx == 2 and locationy == 3:
            locationchange = input("Direction: ")
            if locationchange.lower() == "w":
                locationx -=1
            elif locationchange.lower() == "e":
                locationx +=1
            else:
                print("Not a valid direction!")
    elif locationx == 3 and locationy == 2:
        print("You can travel: (N)orth or (S)outh.")
        while locationx == 3 and locationy == 2:
            locationchange = input("Direction: ")
            if locationchange.lower() == "s":
                locationy -=1
            elif locationchange.lower() == "n":
                locationy +=1
            else:
                print("Not a valid direction!")
print("Victory!")

#prenta út victory ef þetta lendir á réttum stað.n