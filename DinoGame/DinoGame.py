# Making a swag function 
def fullprint(param):
    for i in range(0,len(param)):
        print(' ')
        for k in range(0,len(param[i])):
            print(param[i][k], end=" ")
    print('\n')

gameboard=[
    ["_","#","$","$","$","#","$","$","#","#"],
    ["E","#","#","#","$","#","#","$","$","#"],
    ["_","_","$","$","$","_","_","#","_","$"],
    ["_","_","#","#","$","#","_","_","_","$"],
    ["$","$","$","$","$","#","$","$","#","end"]
]
print("Welcome to DinoGame!")
print("/n")
print("Use the keys w, a, s, d to move your chracter E!")
print("You can move Blocks-*, but not Walls-#, and try to collect all the coins-*!")
fullprint(gameboard)

#Skibidi Toilet Will be mIne
x=1
y=0
Coins=0

gameEnd=False
validinput=False

      
while gameEnd==False:
    validinput=False
    while validinput == False:
            Charactermove=(input("Please move your character:"))
            if Charactermove == "w":
                    if(x-1<0 or gameboard[x-1][y]=="#" ):
                        print("You Can't move there!")
                    else:
                        validinput=True
            

            elif Charactermove == "a":
                if(y-1<0 or gameboard[x][y-1]=="#"):
                        print("You Can't move there!")
                else:
                    validinput=True
            
            elif Charactermove == "s":
                if(gameboard[x+1][y]=="#" or x+1>=len(gameboard)):
                        print("You Can't move there!")
                else:
                    validinput=True
            

            elif Charactermove == "d":
                if(gameboard[x][y+1]=="#" or y+1>=len(gameboard[0])):
                    print("You Can't move there!")
                else:
                    validinput=True
            
            else:
                validinput=True 
    if Charactermove == "w" and gameboard[x-1][y]=="$":
            x-=1
            gameboard[x][y]="E"
            gameboard[x+1][y]="_"
            Coins+=1

    elif Charactermove == "a" and gameboard[x][y-1]=="$":
            y-=1
            gameboard[x][y]="E"
            gameboard[x][y+1]="_"
            Coins+=1

    elif Charactermove == "s" and gameboard[x+1][y]=="$":
            x+=1
            gameboard[x][y]="E"
            gameboard[x-1][y]="_"
            Coins+=1

    elif Charactermove == "d" and gameboard[x][y+1]=="$":
            y+=1
            gameboard[x][y]="E"
            gameboard[x][y-1]="_"
            Coins+=1

    elif Charactermove == "w" and gameboard[x-1][y]=="_":
            x-=1
            gameboard[x][y]="E"
            gameboard[x+1][y]="_"
            
    elif Charactermove == "a" and gameboard[x][y-1]=="_":
            y-=1
            gameboard[x][y]="E"
            gameboard[x][y+1]="_"

    elif Charactermove == "s" and gameboard[x+1][y]=="_":
            x+=1
            gameboard[x][y]="E"
            gameboard[x-1][y]="_"

    elif Charactermove == "d" and gameboard[x][y+1]=="_":
            y+=1
            gameboard[x][y]="E"
            gameboard[x][y-1]="_"
    elif Charactermove == "w" and gameboard[x-1][y]=="end":
            gameEnd=True
            
    elif Charactermove == "a" and gameboard[x][y-1]=="end":
            gameEnd=True

    elif Charactermove == "s" and gameboard[x+1][y]=="end":
            gameEnd=True

    elif Charactermove == "d" and gameboard[x][y+1]=="end":
            gameEnd=True

    else:
        if gameboard[x][y]=="end":
            gameEnd=True
            
    print("Please enter the keys w, a, s, d")
  



    fullprint(gameboard)


print(f"You beat the game with {Coins} coins!")





# "$"=Coins
# "#"=Walls
# "*"=Movable Blocks
#  for hard mode, make the movable blocks so that it would open to more coins
# Move the blocs to the correct spot

