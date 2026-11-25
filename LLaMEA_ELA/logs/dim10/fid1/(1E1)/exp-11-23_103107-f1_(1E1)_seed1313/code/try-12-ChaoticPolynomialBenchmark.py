import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial basin term with mixed degrees
        poly_basin = 0.01 * np.sum(x**6) + 0.1 * np.sum(x**3) + 0.05 * np.sum(x**2)
        
        # Chaotic sinusoidal terms creating irregular landscape
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(15 * x[i]) * np.cos(11 * x[i]) * np.sin(8 * x[i]) + \
                      np.cos(9 * x[i]) * np.sin(6 * x[i]) * np.cos(4 * x[i])
            
        # Cross-term interactions creating complex valleys and ridges
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2) * \
                              np.sin((x[i] + x[j])**2) + \
                              np.cos(x[i] * x[j]) * np.sin(x[i]**3 + x[j]**3)
                
        # Additional chaotic harmonic components with higher frequency
        harmonics = 0
        for i in range(self.dim):
            harmonics += np.sin(7 * x[i]**4) * np.cos(3 * x[i]**3) + \
                        np.cos(5 * x[i]**5) * np.sin(2 * x[i]**4)
        
        # Add a global scaling factor to improve fitness score
        return 0.5 * (poly_basin + chaotic + cross_terms + harmonics) + 0.01 * np.sum(np.abs(x)**7)