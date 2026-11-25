import numpy as np

class SinusoidalBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term with global minimum at origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Sinusoidal oscillations creating multiple local minima
        oscillation_term = 0.0
        for i in range(self.dim):
            oscillation_term += np.sin(3 * x[i]) * np.cos(2 * x[i])
        
        # Additional harmonic terms with varying frequencies and amplitudes
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += 0.5 * np.sin(5 * x[i]) * np.cos(4 * x[i])
            
        # Combine all terms with different weights
        return basin_term + 0.3 * oscillation_term + 0.2 * harmonic_term