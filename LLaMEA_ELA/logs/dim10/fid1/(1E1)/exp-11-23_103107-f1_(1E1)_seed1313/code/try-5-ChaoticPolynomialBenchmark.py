import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial basin term with mixed degrees
        poly_basin = 0.01 * np.sum(x**4) + 0.1 * np.sum(x**2)
        
        # Chaotic sinusoidal terms creating irregular landscape
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
            
        # Cross-term interactions creating complex valleys and ridges
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2)
                
        # Additional chaotic harmonic components
        harmonics = 0
        for i in range(self.dim):
            harmonics += np.sin(5 * x[i]**3) * np.cos(2 * x[i]**2)
            
        return poly_basin + chaotic + cross_terms + harmonics