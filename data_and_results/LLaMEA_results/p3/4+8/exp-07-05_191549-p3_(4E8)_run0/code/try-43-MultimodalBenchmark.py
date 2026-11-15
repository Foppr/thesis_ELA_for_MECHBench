import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with multiple minima
        poly_term = np.sum(x_scaled**4 - 2*x_scaled**2)
        
        # Trigonometric term creating oscillations
        trig_term = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Exponential barrier term to create ruggedness
        exp_term = np.sum(np.exp(-x_scaled**2) * np.sin(3 * np.pi * x_scaled)**2)
        
        # Combine all terms
        return 0.5 * poly_term + 0.3 * trig_term + 0.2 * exp_term