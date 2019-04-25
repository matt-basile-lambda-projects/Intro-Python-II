class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Banjo(Item):
    def __init__(self):
        super().__init__("Banjo", "Your Grandpa Willy's Banjo, he gave it to you to serenade the world!" )
        self.level = 0
    def play(self):
        if(self.level < 3):
            return print("You played a few coarse notes, more practice and you'll get the hang of it!")
        else:
            return print("You're getting purrrtty good yung feller! Starting to sound like music!")
        