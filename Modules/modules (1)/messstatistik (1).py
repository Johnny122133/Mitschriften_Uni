import numpy as np
import math
import pandas

# Messstatistische Grundfunktionen
def weight_mean(Wert, Uns): # gewichteten Mittelwert berechnen
    gew_Mittelw = np.sum(1 / Uns**2 * Wert) / np.sum(1 / Uns**2)
    return gew_Mittelw

def inner_standarddeviation(s_xi): # innere Standardabweichung, returns Varianz, Standardabweichung (=sqrt(Varianz))
    Varianz = 1 / np.sum(1 / s_xi**2)
    Stabw = math.sqrt(Varianz)
    return Varianz, Stabw

def outer_standarddeviation(my, xi, s_xi): # äußerer Standardabweichung, returns Varianz, Standardabweichung (=sqrt(Varianz))
    Varianz = np.sum((xi - my)**2 / s_xi**2) / np.sum(1 / s_xi**2)
    Stabw = math.sqrt(Varianz)
    return Varianz, Stabw

def gaussian_diff(Unsicherheita, Unsicherheitb):    # Gaußsche Fehlerfortpflanzung für Differenz 
    c = np.sqrt(Unsicherheita**2 + Unsicherheitb**2)
    return c

class Messwert:     # class mit Wert und Unsicherheit
    def __init__(self, anz):
        Wert = np.zeros(anz)
        Uns = np.zeros(anz)

def write_csv(data = '', filename = 'out.csv'): # write data to .csv file using a pandas dataframe
    df = pandas.DataFrame(data=np.transpose(data))
    df.to_csv(filename, sep=';', decimal=',')

def write_excel(data = '', filename = 'out.xlsx'):  # write data to .xlsx file using a pandas dataframe
    df = pandas.DataFrame(data=np.transpose(data))
    df.to_excel(filename)

def linear_regression(x_values, y_values, y_deviation):     # calculated linear regression. 
    A= np.sum(1 / (y_deviation**2))
    B= np.sum(x_values / (y_deviation**2))
    C= np.sum(y_values / (y_deviation**2))
    D= np.sum((x_values**2) / (y_deviation**2))
    E= np.sum((x_values*y_values) / (y_deviation**2))

    a1 = (E - (B * C) / A) / (D - (B**2) / A)
    a1_deviation = np.sqrt(D/(A * D - B**2))
    a0 = (C - a1 * B) / A
    a0_deviation = np.sqrt(D / (A * D - B**2))

    return a1, a1_deviation, a0, a0_deviation

def chiquadrat_lin_regr(y_values, y_deviation, x_values, a0, a1):        # Chiquadrat test, a0, a1 from linear regression, returns chiquadrat for linear regression
    return np.sum(((y_values - a0 - a1 * x_values) / y_deviation)**2)
