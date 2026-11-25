import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial and logarithmic base terms
        for i in range(self.dim):
            # Asymmetric polynomial with logarithmic modulation
            if x[i] >= 0:
                result += (x[i]**3) * np.log(1.0 + x[i]**2)
            else:
                result += (x[i]**3) * np.log(1.0 - x[i]**2)
            
            # Trigonometric components with varying frequencies
            result += 1.5 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            result += 0.8 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i])
            
            # Cross-terms creating interaction between dimensions
            if i > 0:
                result += 0.3 * x[i] * x[i-1] * np.exp(-0.1 * (x[i] - x[i-1])**2)
                
        # Multiple global minima with varying depths
        result += 2.0 * np.exp(-0.5 * np.sum((x - 1.0)**2)) + \
                  1.5 * np.exp(-0.3 * np.sum((x + 2.0)**2)) + \
                  1.0 * np.exp(-0.2 * np.sum((x - 3.0)**2))
        
        # Add a ruggedness component with asymmetric peaks
        for i in range(self.dim):
            result += 0.5 * np.sin(7.0 * x[i]) * np.cos(6.0 * x[i]) * (1.0 + 0.1 * x[i]**2)
        
        # Introduce a conditioning effect through weighted exponential terms
        for i in range(self.dim):
            result += 0.2 * np.exp(-0.05 * (x[i] - 0.5)**2) * np.sin(4.0 * x[i])
            
        return result