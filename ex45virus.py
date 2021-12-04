class Virus(object):

    def __init__(self, gas, temp):
        self.gas=gas
        self.temp=temp

    def virus_needs(self):
        print("This virus needs " + self.gas)
        print('and ' + self.temp + " temperature to wake up.")
