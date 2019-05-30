class Map():
    def __init__(self):
        self.dict = {}

    def addInMap(self,arr):
        for i in range(len(arr)):
            name = arr[i].split()
            if name[0] not in self.dict:
                self.dict[name[0]] = [name[1]]
            else:
                self.dict[name[0]].append(name[1])
        return

    def searchName(self, name):
        for key, values in self.dict.items():
            if key == name:
                return True
            for value in values:
                if value == name:
                    return True
        return False

m = Map()
m.addInMap(["Elon Musk", "Ken Howery", "Luke Nosek", "Max Levchin", "Peter Thiel", "Elon Husk"])
print(m.searchName("Howery"))

