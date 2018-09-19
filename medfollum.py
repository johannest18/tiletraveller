#Velja upphafsstaðsetningu x og y
locationx, locationy = 1, 1
location = [locationx, locationy]
#Setja inn færsluaðgerð, þe. setja inn skipanir fyrir færslu og láta kall færast
def faersla(t, f, x, y):
    t = t.lower()
    if t == "n" and n==1:
        y+=1
    elif t == "s" and s ==1:
        y-=1
    elif t == "w" and w == 1:
        x -=1
    elif t == "e" and e == 1:
        x +=1
    else:
        print("Not a valid direction!")
    f = [x, y]
    return f, x, y
#athuga hvort eitthvað sé valid direction

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
#setja inn inputaðgerð
def inputid():
    faerslan = input("Direction: ")
    faerslan = faerslan.lower()
    return faerslan

def heildarfærsla(no, ea, so, we, x, y, xy):
        youcantravel(n, e, s, w)
        location2 = xy
        while location2 == xy:
            attin = inputid()
            xy, x, y = faersla(attin, xy, x, y)      
        return xy, x, y 

victory = [3,1]
while location != victory:
    if location == [1,1] or location == [2,1]:
        n, e, s, w = 1,0,0,0
        location, locationx, locationy = heildarfærsla(n, e, s, w, locationx, locationy, location)
    if location == [1,2]:
        n, e, s, w= 1, 1, 1 ,0
        location, locationx, locationy = heildarfærsla(n, e, s, w, locationx, locationy, location)
    if location == [2,2] or location == [3,3]:
        n, e, s, w= 0, 0, 1 ,1
        location, locationx, locationy = heildarfærsla(n, e, s, w, locationx, locationy, location)
    if location == [1,3]:
        n, e, s, w= 0, 1, 1 ,0
        location, locationx, locationy = heildarfærsla(n, e, s, w, locationx, locationy, location)
    if location == [2,3]:
        n, e, s, w= 0, 1, 0 ,1
        location, locationx, locationy = heildarfærsla(n, e, s, w, locationx, locationy, location)
    if location == [3,2]:
        n, e, s, w= 1, 0, 1 ,0
        location, locationx, locationy = heildarfærsla(n, e, s, w, locationx, locationy, location)
print("Victory!")
#Setja inn færsluaðgerð, þe. setja inn skipanir fyrir færslu og láta kall færast
#Setja inn hvað gerjst gerist í hverjum af 9 tælum
#Setja inn rettar prent skipanir og biðji um input á réttum stöðum

#prenta út victory ef þetta lendir á réttum stað.