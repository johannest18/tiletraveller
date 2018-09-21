#1. það var auðveldara að búa til þessa gerð forrits því það var minna af endurtekningum. Þessi var flóknari en samt auðveldara að búa þetta til
#2. Ég held þessi sé læsilegri. 
#3. Helsti kostur seinni gerðar forritsins er að ef það þarf að stækka svæðið sem ferðast má um eða breyta því þá er það mjög einfalt
#í þessari seinni gerð. Í fyrri gerðinni var það mjög mikil handavinna.

#Setja inn prentaðgerð
def youcantravel(n, e, s, w):
    """Þetta fall athugar í hvaða áttir má færast og segir notanda það"""
    message="You can travel: "
    if n == 1:
        message += "(N)orth"
    if e == 1 and n == 1:
        message += " or (E)ast"
    elif e == 1 and n != 1:
        message += "(E)ast"
    if s == 1 and (n==1 or e ==1):
        message += " or (S)outh"
    elif s == 1 and not (n==1 or e ==1):
        message += "(S)outh"
    if w == 1 and (n==1 or e==1 or s==1):
        message += " or (W)est"
    elif w==1 and not  (n==1 or e==1 or s==1):
        message += "(W)est"
    print(message+".")

#setja inn inputaðgerð
def inputid():
    """Þetta fall biður um input frá notanda og tekur við inputi"""
    faerslan = input("Direction: ")
    faerslan = faerslan.lower()
    return faerslan

#Setja inn færsluaðgerð, þe. setja inn skipanir frá inputi og láta kall færast
def faersla(t, f, x, y):
    """Þetta fall tekur input úr inputfalli, athugar hvort sú átt sem beðið var um sé leyfileg og færir kallinn í þá átt"""
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

def heildarfærsla(no, ea, so, we, x, y, xy):
    """Þetta fall tekur við upplýsingum um í hvaða áttir má færast, og upphafsstaði og lætur öll hin föllin vinna saman að því
    að láta notanda vita í hvaða átt má fara, taka við input og færa kall í leyfilega átt"""
    youcantravel(n, e, s, w)
    location2 = xy
    while location2 == xy:
        attin = inputid()
        xy, x, y = faersla(attin, xy, x, y)      
    return xy, x, y 


#Velja upphafsstaðsetningu x og y
locationx, locationy = 1, 1
location = [locationx, locationy]

#Setja inn hvað gerjst gerist í hverjum af 9 tælum
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
#prenta út victory ef þetta lendir á réttum stað.
print("Victory!")