import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with varied exponents and weights
        poly_term = 0.4 * np.sum(x**2) + 0.05 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Modified sinusoidal oscillations with higher frequencies and phase shifts
        sin_term = np.sum(np.sin(12.0 * x + np.pi/4)) + 0.5 * np.sum(np.cos(7.0 * x - np.pi/3))
        
        # Enhanced cross-term interactions with nonlinear coupling
        cross_term = 0.3 * np.sum(x[:-1] * x[1:] ** 2) + 0.1 * np.sum(x[:-2] * x[2:])
        
        # Additional cubic cross-term with asymmetric weighting for complexity
        cubic_cross = 0.2 * np.sum((x[:-1] * x[1:]) ** 3) + 0.1 * np.sum((x[:-2] + x[2:]) ** 3)
        
        # Radial symmetry breaking term using exponential decay
        radial_term = 0.05 * np.exp(-0.1 * np.sum(x**2))
        
        # Combine all terms
        result = poly_term + sin_term + cross_term + cubic_cross + radial_term
        
        return result