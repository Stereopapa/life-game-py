from organisms.organism import Organism
import random


class Animal(Organism):
    def action(self):
        self.increaseAge()
        move = random.randint(0, 7)
        flag = 0
        while flag < 8:
            afterMove = self.pickPosition(move)
            if (self._worldI.isOrganismInBounds(afterMove)):
                other = self._worldI.getOrganism(afterMove)
                self.setPosition(afterMove)
                if (other != None):
                    other.colision(self)
                return
            move += 1
            move %= 8
            flag += 1

    def breed(self, attacker: Organism):
        move: int = random.randint(0, 7)
        flag: int = 0
        while flag < 8:
            afterMove = self.pickPosition(move)
            if (self._worldI.isOrganismInBounds(afterMove) and self._worldI.getOrganism(afterMove) == None):
                self._worldI.addOrganism(self.__class__.__module__, self.__class__.__name__, afterMove)
                self._worldI.addLog(self.getMark() + " Rozmnożył się ")
                return
            move += 1
            move %= 8
            flag += 1

    def colision(self, attacker: Organism):
        if attacker == self:
            return
        elif type(attacker) == type(self):
            attacker.undoMove()
            if self.getAge() < 2 or attacker.getAge() < 2:
                return
            self.breed(attacker)
        elif self.hasEscaped() or attacker.hasEscaped():
            return
        elif (self.getStrenght() > attacker.getStrenght()):
            attacker.kill()
            self._worldI.addLog(self.getMark() + " zabił " + attacker.getMark())
        else:
            self.kill()
            self._worldI.addLog(attacker.getMark() + " zabił " + self.getMark())
