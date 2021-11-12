class Cars(object):
   

    def __init__(self, brand, model, colour,gearbox, speedLimit):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.gearbox = gearbox
        self.speedLimit = speedLimit


    def start(self):
        print('started')

    def stop(self):
        print('stopped')

    def moving(self):
        print('moving')

Audi = Cars('Audi', 'r8','white','automatic','333km/h')
Toyota = Cars('Toyota','Supra','red','sequential','249km/h')


print(Audi.stop())

print(Toyota.colour)

print(Toyota.gearbox)

print(Toyota.speedLimit)