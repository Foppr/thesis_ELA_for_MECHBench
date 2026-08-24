import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with slight asymmetry
        quadratic = np.sum(x_norm**2) * (1.0 + 0.1 * np.sin(x_norm[0]))
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(13 * x_norm[i]) * np.cos(11 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Asymmetric saddle points with nested structure
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i] - 0.3)**2 * (x_norm[i] + 0.3)**2 * np.cos(5 * np.pi * x_norm[i])
        
        # Fractal-like irregularities using multiple frequency components
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2**i * np.pi * x_norm[i]) * np.cos(3**i * np.pi * x_norm[i])
        
        # Cross-dimensional interaction with non-linear coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.05 * np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[j]) * (1 + 0.1 * np.sin(x_norm[i] + x_norm[j]))
        
        # Add global shift to make global optimum non-trivial
        shift = 0.5 * np.sum(np.sin(2 * np.pi * x_norm))
        
        # Combine all components with different weights
        return 0.4 * quadratic + 0.3 * chaotic + 0.2 * saddle + 0.05 * fractal + 0.03 * interaction + 0.02 * shift + 1.0