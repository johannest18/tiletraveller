#Velja upphafsstaðsetningu x og y
locationx, locationy = 1, 1
location = [locationx, locationy]
#Setja inn færsluaðgerð, þe. setja inn skipanir fyrir færslu og láta kall færast
def faersla(s, x, y):
    s = s.lower()
    if validdirection == 1:
        if s == "n":
            x+=1
        elif s == "s":
            x-=1
        elif s == "w":
            y -=1
        elif s == "e":
            y +=1
    else:
        print("Not a valid direction!")
    return x, y

#Setja inn prentaðgerð
def youcantravel(n, e, s, w):
    message="You can travel: "
    if n == 1:
        message += "(N)orth"
    if e == 1:
        message += " or (E)ast"
    if s == 1:
        message += " or (S)outh"
    if w == 1:
        message += " or (W)est"
    print(message+".")
        
victory = locationx == [3,1]
if not victory:
    youcantravel(1, 1, 0 ,0)
    

#Setja inn færsluaðgerð, þe. setja inn skipanir fyrir færslu og láta kall færast
#Setja inn hvað gerjst gerist í hverjum af 9 tælum
#Setja inn rettar prent skipanir og biðji um input á réttum stöðum

#prenta út victory ef þetta lendir á réttum stað.n
siggi = "n"
validdirection = 1
locationx, locationy = faersla(siggi, locationx, locationy)
print(locationx, locationy)
locationx, locationy = faersla(siggi, locationx, locationy)
print(locationx, locationy)