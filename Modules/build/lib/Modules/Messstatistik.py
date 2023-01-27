import numpy as np
import math
import pandas

def calc_gewichteter_Mittelwert(Wert, Uns):
    gew_Mittelw = np.sum(1/Uns**2 * Wert)/np.sum(1/Uns**2)
    return gew_Mittelw

def calc_innere_Stabw(s_xi): # returns Varianz, Stabw
    Varianz = 1/np.sum(1/s_xi**2)
    Stabw = math.sqrt(Varianz)
    return Varianz, Stabw

def calc_externe_Stabw(my, xi, s_xi): # returns Varianz, Stabw
    Varianz = np.sum((xi-my)**2/s_xi**2)/np.sum(1/s_xi**2)
    Stabw = math.sqrt(Varianz)
    return Varianz, Stabw

def calc_uns_diff(a, b):
    c = np.sqrt(a**2 + b**2)
    return c

class Messwert:
    def __init__(self, anz):
        Wert = np.zeros(anz)
        Uns = np.zeros(anz)

def write_csv(data = '', filename = 'out.csv'):
    df = pandas.DataFrame(data=np.transpose(data))
    df.to_csv(filename, sep=';', decimal=',')

def write_excel(data = '', filename = 'out.xlsx'):
    df = pandas.DataFrame(data=np.transpose(data))
    df.to_excel(filename)