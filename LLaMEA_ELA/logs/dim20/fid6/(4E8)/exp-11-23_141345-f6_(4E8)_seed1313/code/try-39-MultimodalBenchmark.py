import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with higher degree and radial component
        poly_term = np.sum(x**8) + 0.1 * np.sum(x**4)
        
        # Sinusoidal oscillations with multiple frequencies and radial interaction
        sin_term = np.sum(np.sin(2.0 * x) * np.sin(1.5 * x) * np.sin(0.5 * x)) + \
                   0.5 * np.sum(np.sin(3.0 * x) * np.sin(0.7 * x)) + \
                   0.3 * np.sum(np.sin(0.2 * x) * np.sin(1.8 * x))
        
        # Cross-term interactions with different powers and radial symmetry
        cross_term = np.sum(x[:-1]**4 * x[1:]**4) + \
                     0.5 * np.sum(x**3 * np.roll(x, 1)**3) + \
                     0.2 * np.sum(np.abs(x[:-1]) * np.abs(x[1:]))
        
        # Radial symmetry component
        radial_term = 0.1 * (np.sum(x**2))**2
        
        # Combined function with adjusted weights for better fitness
        return 0.15 * poly_term + 0.4 * sin_term + 0.2 * cross_term + 0.1 * radial_term