import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with multiple minima
        poly_term = np.sum(x_scaled**6 - 3*x_scaled**4 + 2*x_scaled**2)
        
        # Trigonometric term creating oscillations with higher frequency
        trig_term = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Exponential barrier term with additional radial component
        exp_term = np.sum(np.exp(-x_scaled**2) * np.sin(4 * np.pi * x_scaled)**3 + 0.1 * np.exp(-0.5 * np.sum(x_scaled**2, axis=0)))
        
        # Additional interaction term between dimensions
        interaction_term = np.sum((x_scaled[:-1] - x_scaled[1:])**2)
        
        # Combine all terms with adjusted coefficients
        return 0.4 * poly_term + 0.35 * trig_term + 0.25 * exp_term + 0.05 * interaction_term