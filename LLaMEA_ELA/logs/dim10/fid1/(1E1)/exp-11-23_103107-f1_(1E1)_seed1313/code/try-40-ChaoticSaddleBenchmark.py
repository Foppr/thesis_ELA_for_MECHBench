import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        chaotic = np.sum(np.sin(10 * x) * np.cos(7 * x) * np.exp(-0.1 * x**2))
        
        # Saddle point structure with asymmetric basins
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 2*x[i] + 1) * np.sin(5 * x[i]) + \
                     (x[i]**3 - x[i]) * np.cos(3 * x[i])
        
        # Asymmetric penalty regions with multiple local minima
        penalty = 0
        for i in range(self.dim):
            if x[i] < 0:
                penalty += 10 * np.exp(-0.5 * (x[i] + 2)**2) * np.sin(4 * x[i])**2
            else:
                penalty += 5 * np.exp(-0.3 * (x[i] - 1)**2) * np.cos(6 * x[i])**2
        
        # Cross-dimensional coupling with chaotic interactions
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited range for locality
                cross += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                        np.exp(-0.2 * (x[i]**2 + x[j]**2)) * \
                        (1 + 0.3 * np.sin(2 * (x[i] + x[j])))
        
        # Combine all components with different weights
        return 0.8 * chaotic + 0.6 * saddle + 0.7 * penalty + 0.9 * cross