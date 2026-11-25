import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher degree interactions
        polynomial = np.sum(x**2) + 0.15 * np.sum(x**4) + 0.05 * np.sum(x**6)
        
        # Enhanced sinusoidal perturbations with varying frequencies and phase shifts
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += (np.sin(6.0 * x[i]) * np.cos(3.0 * x[(i + 1) % self.dim]) + 
                          0.5 * np.sin(4.0 * x[i]) * np.sin(2.0 * x[(i + 2) % self.dim]))
            
        # Additional interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Combine all terms with adjusted weights
        return polynomial + 0.6 * sinusoidal + 0.2 * interaction + 0.1 * np.sum(np.abs(x))