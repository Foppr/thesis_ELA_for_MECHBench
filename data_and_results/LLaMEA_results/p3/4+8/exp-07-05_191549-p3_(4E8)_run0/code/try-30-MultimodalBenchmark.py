import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with multiple minima and interaction
        poly_term = np.sum(x_scaled**6 - 3*x_scaled**4 + 2*x_scaled**2)
        
        # Enhanced trigonometric term with multiple frequencies
        trig_term = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * np.sin(3 * np.pi * x_scaled))
        
        # Exponential barrier term with adaptive scaling
        exp_term = np.sum(np.exp(-2 * x_scaled**2) * (np.sin(4 * np.pi * x_scaled)**2 + 0.5 * np.cos(8 * np.pi * x_scaled)**2))
        
        # Additional interaction term for increased complexity
        interaction_term = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled) * x_scaled**2)
        
        # Combine all terms with optimized weights
        return 0.4 * poly_term + 0.3 * trig_term + 0.2 * exp_term + 0.1 * interaction_term