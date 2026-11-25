import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Modified polynomial basin term with different weights and degrees
        poly_basin = 0.03 * np.sum(x**6) + 0.12 * np.sum(x**3) + 0.09 * np.sum(x**2)
        
        # Chaotic sinusoidal terms with altered frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(20 * x[i]) * np.cos(16 * x[i]) * np.sin(12 * x[i]) + \
                      np.cos(14 * x[i]) * np.sin(11 * x[i]) * np.cos(8 * x[i])
            
        # Modified cross-term interactions with different trigonometric combinations
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2) * \
                              np.cos((x[i] + x[j])**2) + \
                              np.cos(x[i] * x[j]) * np.sin(x[i]**3 + x[j]**3) * \
                              np.sin(x[i]**2 * x[j])
                
        # Modified harmonic components with different powers and frequencies
        harmonics = 0
        for i in range(self.dim):
            harmonics += np.sin(10 * x[i]**4) * np.cos(5 * x[i]**3) + \
                        np.cos(8 * x[i]**5) * np.sin(4 * x[i]**4)
        
        # Added sinusoidal coupling term between dimensions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Add a global scaling factor to improve fitness score
        return 0.65 * (poly_basin + chaotic + cross_terms + harmonics + coupling)