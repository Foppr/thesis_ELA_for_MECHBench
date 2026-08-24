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
        f2 = np.sum(np.sin(9 * np.pi * x_normalized)**2)
        
        # Sum of exponential terms with different decay rates
        f3 = np.sum(np.exp(-x_normalized**2) * np.cos(5 * np.pi * x_normalized))
        
        # Add interaction terms between dimensions with higher coupling strength
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_normalized[i] - x_normalized[j])**6
        
        # Combine all terms with different weights
        result = 0.35 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * interaction
        
        # Add a global minimum at a shifted position with higher-order polynomial
        shift = 0.1
        result += 0.03 * np.sum((x_normalized - shift)**8)
        
        return result