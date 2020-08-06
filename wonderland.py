import random

print("WONDERLAND")

tilecount = 0

turncount = 1

count = 0

countcard = 0

Yside = ""

Rfirstturns = ["S1", "S2", "S3"]
Yfirstturns = ["T1", "T2", "T3"]
turnsafterstable = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
turnsafter = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

cakecards = ["Y1", "Y2", "Y3", "Y5", "Y6"]

possiblenextturn = []

Y1values = {"value" : 1, "side 1" : 2, "side 2" : 1, "side 3" : 1, "side 4" : 0, "color" : "yellow"}
Y2values = {"value" : 2, "side 1" : 2, "side 2" : 0, "side 3" : 1, "side 4" : 1, "color" : "yellow"}
Y3values = {"value" : 3, "side 1" : 2, "side 2" : 1, "side 3" : 1, "side 4" : 2, "color" : "yellow"}
Y4values = {"value" : 4, "side 1" : 0, "side 2" : 1, "side 3" : 1, "side 4" : 1, "color" : "yellow"}
Y5values = {"value" : 5, "side 1" : 2, "side 2" : 1, "side 3" : 1, "side 4" : 1, "color" : "yellow"}
Y6values = {"value" : 6, "side 1" : 1, "side 2" : 2, "side 3" : 1, "side 4" : 1, "color" : "yellow"}
Y7values = {"value" : 7, "side 1" : 1, "side 2" : 1, "side 3" : 1, "side 4" : 1, "color" : "yellow"}
R1values = {"value" : 1, "side 1" : 0, "side 2" : 2, "side 3" : 1, "side 4" : 1, "color" : "red"}
R2values = {"value" : 2, "side 1" : 0, "side 2" : 1, "side 3" : 1, "side 4" : 2, "color" : "red"}
R3values = {"value" : 3, "side 1" : 2, "side 2" : 2, "side 3" : 1, "side 4" : 1, "color" : "red"}
R4values = {"value" : 4, "side 1" : 1, "side 2" : 0, "side 3" : 1, "side 4" : 1, "color" : "red"}
R5values = {"value" : 5, "side 1" : 1, "side 2" : 2, "side 3" : 1, "side 4" : 1, "color" : "red"}
R6values = {"value" : 6, "side 1" : 2, "side 2" : 1, "side 3" : 1, "side 4" : 1, "color" : "red"}
R7values = {"value" : 7, "side 1" : 1, "side 2" : 1, "side 3" : 1, "side 4" : 1, "color" : "red"}

boardRow1 = ["NA", "T1", "T2", "T3"]
boardRow2 = ["S1", "A1", "A2", "A3"]
boardRow3 = ["S2", "B1", "B2", "B3"]
boardRow4 = ["S3", "C1", "C2", "C3"]


tilesaroundA1 = {"side 1" : None, "side 2": "A2", "side 3": "B1", "side 4" : None}
tilesaroundA2 = {"side 1" : None, "side 2": "A3", "side 3": "B2", "side 4" : "A1"}
tilesaroundA3 = {"side 1" : None, "side 2": None, "side 3": "B3", "side 4" : "A2"}
tilesaroundB1 = {"side 1" : "A1", "side 2": "B2", "side 3": "C1", "side 4" : None}
tilesaroundB2 = {"side 1" : "A2", "side 2": "A3", "side 3": "C2", "side 4" : "B1"}
tilesaroundB3 = {"side 1" : "A3", "side 2": None, "side 3": "C3", "side 4" : "B2"}
tilesaroundC1 = {"side 1" : "B1", "side 2": "C2", "side 3": None, "side 4" : None}
tilesaroundC2 = {"side 1" : "B2", "side 2": "C3", "side 3": None, "side 4" : "C1"}
tilesaroundC3 = {"side 1" : "B3", "side 2": None, "side 3": None, "side 4" : "C2"}

class card:
    def getValue(self, valuedict):
        self.value = valuedict["value"]
        self.side1value = valuedict["side 1"]
        self.side2value = valuedict["side 2"]
        self.side3value = valuedict["side 3"]
        self.side4value = valuedict["side 4"]
        self.color = valuedict["color"]

    def rotate(self, valuedict):
        self.side1value = valuedict["side 3"]
        self.side2value = valuedict["side 4"]
        self.side3value = valuedict["side 1"]
        self.side4value = valuedict["side 2"]

    def getPos(self, position):
        self.position = position

color = input("Color (Red or Yellow): ")

RboardRow1 = boardRow1
YboardRow1 = boardRow1
RboardRow2 = boardRow2
YboardRow2 = boardRow2
RboardRow3 = boardRow3
YboardRow3 = boardRow3
RboardRow4 = boardRow4
YboardRow4 = boardRow4

def RprintBoard():
    print(RboardRow1)
    print(RboardRow2)
    print(RboardRow3)
    print(RboardRow4)

def YprintBoard():
    print(YboardRow1)
    print(YboardRow2)
    print(YboardRow3)
    print(YboardRow4)

turn = "red"

Ravailblecards = ["R1", "R2", "R3", "R4", "R5", "R6", "R7"]
Yavailblecards = ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7"]

R1 = card()
R2 = card()
R3 = card()
R4 = card()
R5 = card()
R6 = card()
R7 = card()

Y1 = card()
Y2 = card()
Y3 = card()
Y4 = card()
Y5 = card()
Y6 = card()
Y7 = card()

while turncount <= 14:
    if turncount % 2 != 0:
        turncount = turncount + 1
        RprintBoard()
        count = 0
        command = input("command: ")
        if command == "view cards":
            print(Ravailblecards)
        if command == "play cards":
            print(Ravailblecards)
            countcard = 0
            card = input("select card: ")
            while card not in Ravailblecards:
                card = input("select card")
            if card in Ravailblecards:
                for cardcount in Ravailblecards:
                    if cardcount == card:
                        Ravailblecards.pop(count)
                    count = count + 1
            if turncount <= 6:
                print(Rfirstturns)
                count = 0
                posplace = input("choose between above: ")
                while posplace not in Rfirstturns:
                    posplace = input("pick again: ")
                if posplace in Rfirstturns:
                    for tile in Rfirstturns:
                        if tile == posplace:
                            Rfirstturns.pop(count)
                        count = count + 1
            else:
                count = 0
                print(turnsafter)
                posplace = input("choose from above: ")
                while posplace not in turnsafter:
                    posplace = input("pick again: ")
                if posplace in turnsafter:
                    for tile in turnsafter:
                        if tile == posplace:
                            turnsafter.pop(count)
                        count = count + 1
            if posplace in RboardRow1:
                tilecount = 0
                for tile in RboardRow1:
                    if tile == posplace:
                        RboardRow1[tilecount] = card
                    tilecount = tilecount + 1
            if posplace in RboardRow2:
                tilecount = 0
                for tile in RboardRow2:
                    if tile == posplace:
                        RboardRow2[tilecount] = card
                    tilecount = tilecount + 1
            if posplace in RboardRow3:
                tilecount = 0
                for tile in RboardRow3:
                    if tile == posplace:
                        RboardRow3[tilecount] = card
                    tilecount = tilecount + 1
            if posplace in RboardRow4:
                tilecount = 0
                for tile in RboardRow4:
                    if tile == posplace:
                        RboardRow4[tilecount] = card
                    tilecount = tilecount + 1
            RprintBoard()
            if card == "R1":
                R1.getPos(posplace)
            elif card == "R2":
                R2.getPos(posplace)
            elif card == "R3":
                R3.getPos(posplace)
            elif card == "R4":
                R4.getPos(posplace)
            elif card == "R5":
                R5.getPos(posplace)
            elif card == "R6":
                R6.getPos(posplace)
            elif card == "R7":
                R7.getPos(posplace)



    if turncount % 2 == 0:
        print("Computer Turn")
        if turncount <= 6:
            card = random.choice(Yavailblecards)
            posplaceY = Yfirstturns[0]
            Yfirstturns.pop(0)
            count = 0
            for a in Yavailblecards:
                if a == card:
                    Yavailblecards.pop(count)
                count = count + 1
        elif turncount == 8:
            card = random.choice(Yavailblecards)
            posplaceY = random.choice(turnsafter)
            count = 0
            for a in Yavailblecards:
                if a == card:
                    Yavailblecards.pop(count)
                count = count + 1
        elif turncount >= 10:
            possiblenextturn.clear()
            count = 0
            if posplaceY == "A1":
                possiblenextturn.append(tilesaroundA1["side 1"])
                possiblenextturn.append(tilesaroundA1["side 2"])
                possiblenextturn.append(tilesaroundA1["side 3"])
                possiblenextturn.append(tilesaroundA1["side 4"])
                for entry in possiblenextturn:
                    if entry == None:
                        possiblenextturn.pop(count)
                    count = count + 1
            if posplaceY == "A2":
                possiblenextturn.append(tilesaroundA2["side 1"])
                possiblenextturn.append(tilesaroundA2["side 2"])
                possiblenextturn.append(tilesaroundA2["side 3"])
                possiblenextturn.append(tilesaroundA2["side 4"])
                for entry in possiblenextturn:
                    if entry == None:
                        possiblenextturn.pop(count)
                    count = count + 1
            if posplaceY == "A3":
                possiblenextturn.append(tilesaroundA3["side 1"])
                possiblenextturn.append(tilesaroundA3["side 2"])
                possiblenextturn.append(tilesaroundA3["side 3"])
                possiblenextturn.append(tilesaroundA3["side 4"])
                for entry in possiblenextturn:
                    if entry == None:
                        possiblenextturn.pop(count)
                    count = count + 1
            if posplaceY == "B1":
                possiblenextturn.append(tilesaroundB1["side 1"])
                possiblenextturn.append(tilesaroundB1["side 2"])
                possiblenextturn.append(tilesaroundB1["side 3"])
                possiblenextturn.append(tilesaroundB1["side 4"])
                for entry in possiblenextturn:
                    if entry == None:
                        possiblenextturn.pop(count)
                    count = count + 1
            if posplaceY == "B2":
                possiblenextturn.append(tilesaroundB2["side 1"])
                possiblenextturn.append(tilesaroundB2["side 2"])
                possiblenextturn.append(tilesaroundB2["side 3"])
                possiblenextturn.append(tilesaroundB2["side 4"])
                for entry in possiblenextturn:
                    if entry == None:
                        possiblenextturn.pop(count)
                    count = count + 1
            if posplaceY == "B3":
                possiblenextturn.append(tilesaroundB3["side 1"])
                possiblenextturn.append(tilesaroundB3["side 2"])
                possiblenextturn.append(tilesaroundB3["side 3"])
                possiblenextturn.append(tilesaroundB3["side 4"])
                for entry in possiblenextturn:
                    if entry == None:
                        possiblenextturn.pop(count)
                    count = count + 1
            if posplaceY == "C1":
                possiblenextturn.append(tilesaroundC1["side 1"])
                possiblenextturn.append(tilesaroundC1["side 2"])
                possiblenextturn.append(tilesaroundC1["side 3"])
                possiblenextturn.append(tilesaroundC1["side 4"])
                for entry in possiblenextturn:
                    if entry == None:
                        possiblenextturn.pop(count)
                    count = count + 1
            if posplaceY == "C2":
                possiblenextturn.append(tilesaroundC2["side 1"])
                possiblenextturn.append(tilesaroundC2["side 2"])
                possiblenextturn.append(tilesaroundC2["side 3"])
                possiblenextturn.append(tilesaroundC2["side 4"])
                for entry in possiblenextturn:
                    if entry == None:
                        possiblenextturn.pop(count)
                    count = count + 1
            if posplaceY == "C3":
                possiblenextturn.append(tilesaroundC3["side 1"])
                possiblenextturn.append(tilesaroundC3["side 2"])
                possiblenextturn.append(tilesaroundC3["side 3"])
                possiblenextturn.append(tilesaroundC3["side 4"])
                for entry in possiblenextturn:
                    if entry == None:
                        possiblenextturn.pop(count)
                    count = count + 1
            count = 0
            for tile in possiblenextturn:
                if tile not in turnsafter:
                    possiblenextturn.pop(count)
                count = count + 1
            count = 0
            for card in cakecards:
                if card not in Yavailblecards:
                    cakecards.pop(count)
                count = count + 1

            Ynextturn = random.choice(possiblenextturn)


            if posplaceY == "A1":
                for key in tilesaroundA1:
                    if tilesaroundA1[key] == Ynextturn:
                        Yside = key
               
            if posplaceY == "A2":
                for key in tilesaroundA2:
                    if tilesaroundA2[key] == Ynextturn:
                        Yside = key
                
            if posplaceY == "A3":
                for key in tilesaroundA3:
                    if tilesaroundA3[key] == Ynextturn:
                        Yside = key
                
            if posplaceY == "B1":
                for key in tilesaroundB1:
                    if tilesaroundB1[key] == Ynextturn:
                        Yside = key
                
            if posplaceY == "B2":
                for key in tilesaroundB2:
                    if tilesaroundB2[key] == Ynextturn:
                        Yside = key
                
            if posplaceY == "B3":
                for key in tilesaroundB3:
                    if tilesaroundB3[key] == Ynextturn:
                        Yside = key
                
            if posplaceY == "C1":
                for key in tilesaroundC1:
                    if tilesaroundC1[key] == Ynextturn:
                        Yside = key
                
            if posplaceY == "C2":
                for key in tilesaroundC2:
                    if tilesaroundC2[key] == Ynextturn:
                        Yside = key
                
            if posplaceY == "C3":
                for key in tilesaroundC3:
                    if tilesaroundC3[key] == Ynextturn:
                        Yside = key
        
            card = ""


            if Yside == "side 1":
                Yside = "side 3"
            elif Yside == "side 2":
                Yside = "side 4"
            elif Yside == "side 3":
                Yside = "side 1"
            elif Yside == "side 4":
                Yside = "side 2"         

            for b in cakecards:
                if b == "Y1":
                    if Y1values[Yside] == 2:
                        card = b
                elif b == "Y2":
                    if Y2values[Yside] == 2:
                        card = b
                elif b == "Y3":
                    if Y3values[Yside] == 2:
                        card = b
                elif b == "Y5":
                    if Y5values[Yside] == 2:
                        card = b
                elif b == "Y6":
                    if Y6values[Yside] == 2:
                        card = b


            if card == "":
                card = random.choice(Yavailblecards)


            posplaceY = Ynextturn

        if posplaceY in RboardRow1:
            tilecount = 0
            for tile in RboardRow1:
                if tile == posplaceY:
                    RboardRow1[tilecount] = "Y"
                tilecount = tilecount + 1
        if posplaceY in RboardRow2:
            tilecount = 0
            for tile in RboardRow2:
                if tile == posplaceY:
                    RboardRow2[tilecount] = "Y"
                tilecount = tilecount + 1
        if posplaceY in RboardRow3:
            tilecount = 0
            for tile in RboardRow3:
                if tile == posplaceY:
                    RboardRow3[tilecount] = "Y"
                tilecount = tilecount + 1
        if posplaceY in RboardRow4:
            tilecount = 0
            for tile in RboardRow4:
                if tile == posplaceY:
                    RboardRow4[tilecount] = "Y"
                tilecount = tilecount + 1

        if card == "Y1":
            Y1.getPos(posplaceY)
        elif card == "Y2":
            Y2.getPos(posplaceY)
        elif card == "Y3":
            Y3.getPos(posplaceY)
        elif card == "Y4":
            Y4.getPos(posplaceY)
        elif card == "Y5":
            Y5.getPos(posplaceY)
        elif card == "Y6":
            Y6.getPos(posplaceY)
        elif card == "Y7":
            Y7.getPos(posplaceY)

        count = 0
        for pos in turnsafter:
            if pos == posplaceY:
                turnsafter.pop(count)
            count = count + 1
        turncount = turncount + 1
