import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Quadratic base with varying weights
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal components with phase shifts
        f2 = np.sum(np.sin(7 * np.pi * x_normalized) * np.cos(5 * np.pi * x_normalized))
        
        # Exponential decay with sinusoidal modulation
        f3 = np.sum(np.exp(-3 * x_normalized**2) * np.sin(6 * np.pi * x_normalized))
        
        # Complex interaction terms with asymmetric coupling and higher-order polynomials
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction with cubic and quadratic terms
                interaction += (x_normalized[i]**4 - x_normalized[j]**3)**2 + 0.5 * (x_normalized[i]**2 - x_normalized[j])**4
        
        # Global minimum with polynomial and periodic components
        result = 0.25 * f1 + 0.3 * f2 + 0.2 * f3 + 0.25 * interaction
        
        # Stronger periodic modulation to increase local minima density
        periodic_mod = np.sum(np.sin(3 * np.pi * x_normalized) * np.cos(3 * np.pi * x_normalized) + 
                             0.3 * np.sin(9 * np.pi * x_normalized))
        result += 0.1 * periodic_mod
        
        # Enhanced saddle point structure with quartic and sextic terms
        saddle = np.sum(x_normalized**6 - 3 * x_normalized**4 + 2 * x_normalized**2)
        result += 0.05 * saddle
        
        # Add a small noise component to increase problem difficulty
        noise = 0.01 * np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(8 * np.pi * x_normalized))
        result += noise
        
        return result