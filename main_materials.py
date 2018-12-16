

class material():
    ''' This is the materials class function '''


    def __init__(self, name):
        self.name = name # Name of the material
        self.density = 7900      # kg/m^3
        self.conductivity = 10.9 # W/mK

    def describe(self):
        print("Name: {} \nDensity: {} [kg/m^3] \nConductivity: {} [W/mK]".format(self.name,self.density,self.conductivity))


mat = material("Gd")

mat.describe()
