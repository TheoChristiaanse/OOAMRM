# Numpy library
import numpy as np
# Inport  interpolation functions
from scipy.interpolate import RectBivariateSpline as RBS

class material():
    ''' This is the materials class function '''

    def __init__(self, name):
        self.name = name # Name of the material

    def describe(self):
        ''' This function gives a description of the material. '''
        print("Name: {}".format(self.name))

    def cp(self,T,B):
        ''' This function recovers the specific heat [J/kgK] of the material as
        a function of the Temperature [K] and internal field [T].
        T = Temperature [K]
        B = Internal Field Value [T]'''
        try:
            return self.mCp(T,B)[0,0]
        except AttributeError:
            print('You need to load some material data first.')

    def mag(self,T,B):
        ''' This function recovers the magnetic moment per unit mass [Am^2/kg]
        of the material as a function of the Temperature [K] and internal field
        [T].
        T = Temperature [K]
        B = Internal Field Value [T]'''
        try:
            return self.mMag(T,B)[0,0]
        except AttributeError:
            print('You need to load some material data first.')

    def s(self,T,B):
        ''' This function recovers the entropy per unit mass [J/kgK] of the
        material as a function of the Temperature [K] and internal field [T].
        T = Temperature [K]
        B = Internal Field Value [T]'''
        try:
            return self.mStot(T,B)[0,0]
        except AttributeError:
            print('You need to load some material data first.')

    def load_Gd(self,**kwargs):
        ''' This function loads all the material data to run a Gd materialself.
        The material data is based on the MFT simulations. You can shift the
        properties by setting the shift function or the Tcurie to set the Curie
        temperature.
        '''
        if 'shift' in kwargs:
            shift = kwargs['shift']
        if 'Tcurie' in kwargs:
            shift = kwargs['Tcurie']-273
        else:
            shift = 0

        self.name = 'Gd - mft'
        self.density = 7900      # kg/m^3
        self.conductivity = 10.9 # W/mK
        # Specifc Heat
        cp_data   = np.loadtxt('./materials/Gd_mft/gdcp_py.txt')
        # Magnetization
        mag_data = np.loadtxt('./materials/Gd_mft/gdmag_py.txt')
        # Entropy
        stot_data = np.loadtxt('./materials/Gd_mft/gdstot_py.txt')
        # Specifc Heat cooling
        HintCp = cp_data[0, 1:] # Internal Field Values
        TempCp = cp_data[1:, 0]-shift # # Temperature Values
        # Build interpolation function
        self.mCp = RBS(TempCp, HintCp, cp_data[1:, 1:], ky=1, kx=1)
        # Specifc Heat cooling
        HintMag = mag_data[0, 1:] # Internal Field Values
        TempMag = mag_data[1:, 0]-shift # # Temperature Values
        # Build interpolation function
        self.mMag = RBS(TempCp, HintCp, mag_data[1:, 1:], ky=1, kx=1)
        # Specifc Heat cooling
        HintSTot = stot_data[0, 1:] # Internal Field Values
        TempSTot = stot_data[1:, 0]-shift # # Temperature Values
        # Build interpolation function
        self.mStot = RBS(TempCp, HintCp, stot_data[1:, 1:], ky=1, kx=1)



mat = material("Gd")
mat.load_Gd()
print(mat.cp(290,1))
print(mat.cp(292,1))
mat2 = material("Gd")
mat2.load_Gd(shift=2)
print(mat2.cp(290,1))
