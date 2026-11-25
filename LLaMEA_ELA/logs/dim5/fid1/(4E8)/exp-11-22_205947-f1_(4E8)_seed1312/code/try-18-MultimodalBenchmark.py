import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with variable exponents
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Enhanced sinusoidal perturbations with coupled interactions
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += (np.sin(3.0 * x[i]) * np.cos(4.0 * x[(i + 1) % self.dim]) + 
                          0.5 * np.sin(7.0 * x[i]) * np.cos(3.0 * x[(i + 2) % self.dim]))
            
        # Adaptive weight based on dimensionality
        adaptive_weight = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Add a modified Manhattan term for additional complexity
        manhattan = np.sum(np.abs(x)) * (1.0 + 0.05 * np.sin(2.0 * np.sum(x)))
        
        return adaptive_weight * polynomial + 0.3 * sinusoidal + 0.05 * manhattan