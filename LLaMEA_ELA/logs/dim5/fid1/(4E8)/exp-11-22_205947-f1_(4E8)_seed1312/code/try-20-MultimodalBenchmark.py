import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with variable exponents
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Complex sinusoidal perturbations with multiple frequencies and interactions
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += (np.sin(3.0 * x[i]) * np.cos(4.0 * x[(i + 1) % self.dim]) + 
                          np.sin(7.0 * x[i]) * np.cos(3.0 * x[(i + 2) % self.dim]) +
                          np.sin(5.0 * x[i]) * np.sin(2.0 * x[(i + 3) % self.dim]))
        
        # Additional interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.5 * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
        
        # Adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine all terms with different weights and scaling
        return adaptive_scale * (polynomial + 0.3 * sinusoidal + 0.2 * interaction) + 0.15 * np.sum(np.abs(x)) + 0.05 * np.sum(x**8)