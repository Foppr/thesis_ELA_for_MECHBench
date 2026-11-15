import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with different frequencies
        f2 = np.sum(np.sin(7 * np.pi * x_normalized)**2)
        
        # Sum of exponential terms with different decay rates
        f3 = np.sum(np.exp(-x_normalized**2) * np.cos(3 * np.pi * x_normalized))
        
        # Add interaction terms between dimensions with higher coupling strength
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_normalized[i] - x_normalized[j])**4
        
        # Combine all terms with different weights
        result = 0.4 * f1 + 0.35 * f2 + 0.25 * f3 + 0.15 * interaction
        
        # Add a global minimum at the origin with higher-order polynomial
        result += 0.02 * np.sum(x_normalized**6)
        
        return result