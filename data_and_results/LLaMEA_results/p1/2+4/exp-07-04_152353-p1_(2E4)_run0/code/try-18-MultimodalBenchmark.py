import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Quadratic base with conditioning
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal components with varying amplitudes
        f2 = np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(7 * np.pi * x_normalized))
        
        # Multi-scale exponential decay with phase modulation
        f3 = np.sum(np.exp(-3 * x_normalized**2) * np.sin(5 * np.pi * x_normalized) * np.cos(2 * np.pi * x_normalized))
        
        # Asymmetric coupling with higher-order polynomial interactions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction with mixed powers
                interaction += (x_normalized[i]**4 - x_normalized[j]**3)**2 + 0.5 * (x_normalized[i]**2 - x_normalized[j])**4
        
        # Global structure with periodic modulation and polynomial correction
        result = 0.25 * f1 + 0.3 * f2 + 0.2 * f3 + 0.25 * interaction
        
        # Additional periodic modulation to create multiple local minima
        periodic_mod = np.sum(np.sin(3 * np.pi * x_normalized) * np.cos(4 * np.pi * x_normalized))
        result += 0.08 * periodic_mod
        
        # Saddle point structure with negative curvature regions
        saddle = np.sum(x_normalized**6 - 3 * x_normalized**4 + 2 * x_normalized**2)
        result += 0.04 * saddle
        
        # Add a small noise-like component to increase complexity
        noise = np.sum(np.sin(15 * x_normalized) * np.cos(12 * x_normalized))
        result += 0.02 * noise
        
        return result