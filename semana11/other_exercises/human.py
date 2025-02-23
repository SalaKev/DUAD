class Head:
    def describe(self):
        print('head')


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


    def describe(self):
        print('torso')

class Arm:
    def __init__(self, side):
        self.side = side
        self.hand = Hand(side)


    def describe(self):
        print(f'{self.side} arm')
        self.hand.describe()

class Hand:
    def __init__(self, side):
        self.side = side


    def describe(self):
        print(f'{self.side} hand')



class Leg:
    def __init__(self, side):
        self.side = side
        self.feet = Feet(side)


    def describe(self):
        print(f'{self.side} leg')
        self.feet.describe()


class Feet:
    def __init__(self, side):
        self.side = side


    def describe(self):
        print(f'{self.side} foot')



class Human:
    def __init__(self):
        self.right_feet = Feet('right')
        self.left_feet = Feet('left')
        self.right_hand = Hand('right')
        self.left_hand = Hand('left')
        self.right_leg = Leg('right')
        self.left_leg = Leg('left')
        self.right_arm = Arm('right')
        self.left_arm = Arm('left')
        self.head = Head()
        self.torso = Torso(self.head, self.right_arm, self.left_arm, self.right_leg, self.left_leg)


    def describe(self):
        self.head.describe()
        self.torso.describe()
        self.right_arm.describe()
        self.left_arm.describe()
        self.right_leg.describe()
        self.left_leg.describe()


human = Human()
human.describe()
