import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term with varying weights
        f1 = np.sum(x_normalized**2)
        
        # Nested parabolic valleys with different scales
        f2 = np.sum((x_normalized**2 + 0.1 * np.sin(10 * x_normalized))**2)
        
        # Asymmetric saddle points with higher-order polynomial interactions
        f3 = np.sum((x_normalized**3 - 0.5 * x_normalized)**2)
        
        # Composite sinusoidal modulation with varying frequencies
        f4 = np.sum(np.sin(2 * np.pi * x_normalized) * np.cos(3 * np.pi * x_normalized) + 
                   0.5 * np.sin(5 * np.pi * x_normalized) * np.cos(7 * np.pi * x_normalized))
        
        # Cross-terms creating complex interaction patterns
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric coupling with exponential and polynomial terms
                interaction += np.exp(-0.5 * (x_normalized[i] - x_normalized[j])**2) * (x_normalized[i]**3 + x_normalized[j]**2)
        
        # Global minimum structure with polynomial and periodic components
        result = 0.3 * f1 + 0.25 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * interaction
        
        # Enhanced periodic structure with multiple frequencies
        periodic = np.sum(np.sin(4 * np.pi * x_normalized) + 0.3 * np.sin(12 * np.pi * x_normalized) + 
                         0.1 * np.sin(20 * np.pi * x_normalized))
        result += 0.1 * periodic
        
        # Saddle point enhancement with quartic and sextic terms
        saddle = np.sum(x_normalized**4 - 2 * x_normalized**2 + 0.5 * x_normalized**6)
        result += 0.05 * saddle
        
        # Add noise to increase problem difficulty
        noise = 0.02 * np.sum(np.sin(15 * np.pi * x_normalized) * np.cos(13 * np.pi * x_normalized))
        result += noise
        
        return result