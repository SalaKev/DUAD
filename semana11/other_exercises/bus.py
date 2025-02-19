class Bus:
    def __init__(self):
        self.minimum = 0
        self.max_passengers = 6
        self.person = 0

    def add_passenger(self):
        if (self.person >= self.max_passengers):
            print('The bus is full')
            return(self.person)
        elif(self.person < self.max_passengers):
            self.person = self.person + 1
            print('Passenger added!!')
            return(self.person)
        
    def remove_passenger(self):
        if (self.person == self.minimum):
            print('The bus is empty')
            return(self.person)
        elif(self.person > self.minimum):
            self.person = self.person - 1
            print('Passenger removed!!')
            return(self.person)
        
    def main_control(self):
        while (True):
            print('BUS SYSTEM')
            print('Max passengers : 6')
            print('What you want to do?')
            print('1: Add passenger')
            print('2: Remove passenger')
            print('3: Exit')
            self.selection = int(input('Enter the number: '))
            if (self.selection == 1):
                self.person = self.add_passenger()
            if (self.selection == 2):
                self.person = self.remove_passenger()
            if (self.selection == 3):
                print('Bye!')
                print()
                break
            print()

bus = Bus()
bus.main_control()