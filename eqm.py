import numpy as np

def calculate_eqm(y_prediction, y_i):
    eqm=(1/len(y_prediction))*sum((y_prediction-y_i)**2)
    print(eqm)
    return eqm

y_prediction=np.array([1,2,3])
y_i=np.array([0,0,3])

calculate_eqm(y_prediction, y_i)
