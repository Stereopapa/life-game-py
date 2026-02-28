from organisms import Organism
from organisms.animals.animal import Animal
import random

class Human(Animal):
    def __init__(self,position: (int,int),world):
        super().__init__(world, "Człowiek", 5, 4, position)
        self.__specialAbility = 0
        self.__pickedPosition = self._position

    def action(self):
        self.increaseAge()
        if self.__specialAbility != 0:
            if (self.__specialAbility > 0 and self.__specialAbility <5) or self.__specialAbility < 0:
                self.__specialAbility += 1
            else:
                self.__specialAbility = -5
        org = self._worldI.getOrganism(self.__pickedPosition)
        self.setPosition(self.__pickedPosition)
        if org != None and org != self:
            org.colision(self)

    def colision(self, attacker: Organism):
        if self.__specialAbility > 0:
            self._worldI.addLog(self.getMark()+" Odbił atak "+attacker.getMark())
            move: int = random.randint(0, 7)
            flag: int = 0
            while flag < 8:
                afterMove = self.pickPosition(move)
                if (self._worldI.isOrganismInBounds(afterMove) and self._worldI.getOrganism(afterMove) == None):
                    attacker.setPosition(afterMove)
                    return
                move += 1
                move %= 8
                flag += 1
            attacker.undoMove()
        else:
            super().colision(attacker)

    def toSave(self) -> str:
        res: str = super().toSave()
        res.replace("\n", "")
        res += str(self.__specialAbility)+";"
        return res

    def setDirection(self, direction: (int, int)):
        self.__pickedPosition = (self.__pickedPosition[0]+direction[0], self.__pickedPosition[1]+direction[1])
        if not self._worldI.isOrganismInBounds(self.__pickedPosition):
            self.resetDirection()
        return self.__pickedPosition

    def resetDirection(self):
        self.__pickedPosition = self._position

    def getPickedPosition(self):
        return self.__pickedPosition

    def activateSpecialAbility(self):
        if(self.__specialAbility == 0):
            self.__specialAbility += 1

    def getSpecialAbilityState(self):
        if self.__specialAbility > 0 and self.__specialAbility <=5:
            return "Tarcza: Aktywna"
        elif self.__specialAbility < 0:
            return "Tarcza: Ładuje się"
        else:
            return "Tarcza: Gotowa"

    def setSpecialAbility(self, value):
        self.__specialAbility = value
