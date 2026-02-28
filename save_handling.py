import os

from worlds.world import World
from organisms.animals.human import Human
from datetime import datetime

class SaveHandler:
    def __init__(self, world: World):
        self.__world = world

    def getSaves(self) -> str:
        if not os.path.exists("saves.txt"):
            open("saves.txt", "w").close()
        savesFile = open("saves.txt", 'r')
        return savesFile.read()
    def save(self) -> str:
        if not os.path.exists("saves"):
            os.makedirs("saves")

        now = datetime.now()
        d1 = now.strftime("%Y_%m_%d_%H_%M_%S")
        name: str = "save_"+str(d1)+".txt"
        saveString = ""
        saveString += self.__world.toSave()
        for org in self.__world.getOrganisms():
            saveString += org.toSave()+"\n"

        path: str = "saves/"+name
        saveFile = open(path, "w")
        saveFile.write(saveString)
        saveFile.close()

        savesfile = open("saves.txt", "a")
        savesfile.write(name+"\n")
        savesfile.close()

        self.__world.addLog("Człowiek utworzył nowy zapis")
        return name

    def load(self, name: str):
        path: str = "saves/"+name
        try:
            saveFile = open(path, "r")
            line = saveFile.readline()
            while line:
                line = line.split(";")
                if line[0] == "World":
                    self.__world.initWorld(int(line[1]), int(line[2]), int(line[3]))
                elif line[0] == "Human":
                    position: (int, int) = (int(line[4]), int(line[5]))
                    human: Human = self.__world.addOrganism(line[1], line[0], position)
                    human.setAge(int(line[2]))
                    human.increaseStrenght(int(line[3]) - human.getStrenght())
                    human.setSpecialAbility(int(line[6]))
                    self.__world.setHuman(human)
                else:
                    position: (int, int) = (int(line[4]), int(line[5]))
                    org = self.__world.addOrganism(line[1], line[0], position)
                    org.setAge(int(line[2]))
                    org.increaseStrenght(int(line[3])- org.getStrenght())
                line = saveFile.readline()
            saveFile.close()
        except FileNotFoundError:
            print("The file does not exist.")
            return

