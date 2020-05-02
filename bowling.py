import random


class Bowling_Alley:

    def __init__(self):
        self.first_name = str(input("Enter first name of player:"))
        self.last_name = str(input("Enter last name of player:"))
        self.number = int(input("Enter number for player"))
        self.email = self.first_name + "." + self.last_name + "@bowling.alley"

        y = []
        for i in range(10):
            for k in range(2):
                x = random.randint(1, 10)
                if x != 10:
                    z = random.randint(1, 10)
                    x += z
            y.append(x)
        self.score = sum(y)


total = int(input("Enter Total Number of Players"))
for t in range(total):
    player = Bowling_Alley()
    print(player.__dict__)

