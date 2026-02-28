from organisms import Organism
from organisms.animals.animal import Animal
# from worlds.world import World

class CyberSheep(Animal):
    def __init__(self,position: (int,int), world):
        self.name = "CyberSheep"
        super().__init__(world, "CyberOwca", 4, 4, position)
    def action(self):
        pineBorscht = self._worldI.getPineBorscht()
        if pineBorscht == None:
            super().action()
            return

        pineBorschtPosition = pineBorscht.getPosition()
        amountX = (pineBorschtPosition[0]-self._position[0])
        amountY = (pineBorschtPosition[1]-self._position[1])

        if amountX > 0:
            amountX = 1
        elif amountX < 0:
            amountX = -1
        else:
            amountX = 0

        if amountY > 0:
            amountY = 1
        elif amountY < 0:
            amountY = -1
        else:
            amountY = 0

        afterMove = (self._position[0]+amountX, self._position[1]+amountY)
        self.setPosition(afterMove)
        if afterMove == pineBorschtPosition:
            pineBorscht.colision(self)



