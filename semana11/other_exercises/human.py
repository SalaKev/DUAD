class Head:
    def __init__(self):
        print('head')
        pass


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        print('torso')
        pass


class LeftArm:
    def __init__(self, left_hand):
        self.left_hand = left_hand
        print('LArm')
        pass


class RightArm:
    def __init__(self, right_hand):
        self.right_hand = right_hand
        print('RArm')
        pass


class Hand:
    def __init__(self):
        print('hand')
        pass


class LeftLeg:
    def __init__(self, left_feet):
        self.left_feet = left_feet
        print('LLeg')
        pass


class RightLeg:
    def __init__(self, right_feet):
        self.right_feet = right_feet
        print('RLeg')
        pass


class Feet:
    def __init__(self):
        print('feet')
        pass


class Human:
    def __init__(self):
        self.right_feet = Feet()
        self.left_feet = Feet()
        self.right_hand = Hand()
        self.left_hand = Hand()
        self.right_leg = RightLeg(self.right_feet)
        self.left_leg = LeftLeg(self.left_feet)
        self.right_arm = RightArm(self.right_hand)
        self.left_arm = LeftArm(self.left_hand)
        self.head = Head()
        self.torso = Torso(self.head, self.right_arm, self.left_arm, self.right_leg, self.left_leg)
        
        pass
    
human = Human()
