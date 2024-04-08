import numpy as np
def calculate(liste) :
    
    if len(liste) != 9:
        raise ValueError("List must contain nine numbers.")
        
    matrix = np.reshape(liste,(3,3))
    
    return {
      'mean': [list(matrix.mean(1)), list(matrix.mean(0)), np.mean(liste)],
      'variance': [list(matrix.var(1)),list(matrix.var(0)),np.var(liste)],
      'standard deviation': [list(matrix.std(1)),list(matrix.std(0)),np.var(liste)],
      'max': [list(matrix.max(1)),list(matrix.max(0)),np.max(liste)],
      'min': [list(matrix.min(1)),list(matrix.min(0)),np.min(liste)],
      'sum': [list(matrix.sum(1)),list(matrix.sum(0)),np.sum(liste)]
    }
        