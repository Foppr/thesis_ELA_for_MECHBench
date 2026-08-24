import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with different frequencies and phases
        f2 = np.sum(np.sin(5 * np.pi * x_normalized) * np.cos(3 * np.pi * x_normalized))
        
        # Sum of exponential terms with different decay rates and offsets
        f3 = np.sum(np.exp(-2 * x_normalized**2) * np.sin(4 * np.pi * x_normalized))
        
        # Add interaction terms between dimensions with asymmetric coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction term
                interaction += (x_normalized[i]**3 - x_normalized[j]**2)**2
        
        # Add a global minimum with higher-order polynomial and periodic modulation
        result = 0.3 * f1 + 0.3 * f2 + 0.25 * f3 + 0.15 * interaction
        
        # Add a periodic modulation to create multiple local minima
        periodic_mod = np.sum(np.sin(2 * np.pi * x_normalized) * np.cos(2 * np.pi * x_normalized))
        result += 0.05 * periodic_mod
        
        # Add a saddle point structure by introducing negative curvature regions
        saddle = np.sum(x_normalized**4 - 2 * x_normalized**2)
        result += 0.03 * saddle
        
        return result