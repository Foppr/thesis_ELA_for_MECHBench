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
        f2 = np.sum(np.sin(7 * np.pi * x_normalized) * np.cos(4 * np.pi * x_normalized))
        
        # Sum of exponential terms with different decay rates and offsets
        f3 = np.sum(np.exp(-3 * x_normalized**2) * np.sin(5 * np.pi * x_normalized))
        
        # Add interaction terms between dimensions with asymmetric coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction term with higher-order nonlinearity
                interaction += (x_normalized[i]**4 - x_normalized[j]**3)**2
        
        # Add a global minimum with higher-order polynomial and periodic modulation
        result = 0.25 * f1 + 0.35 * f2 + 0.2 * f3 + 0.2 * interaction
        
        # Add a periodic modulation to create multiple local minima
        periodic_mod = np.sum(np.sin(3 * np.pi * x_normalized) * np.cos(3 * np.pi * x_normalized))
        result += 0.08 * periodic_mod
        
        # Add a saddle point structure by introducing negative curvature regions
        saddle = np.sum(x_normalized**5 - 2.5 * x_normalized**2)
        result += 0.05 * saddle
        
        return result