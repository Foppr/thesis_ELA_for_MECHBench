import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add quadratic term for conditioning
        result += 0.3 * np.sum(x**2)
        
        # Add periodic terms with varying frequencies and chaotic modulation
        for i in range(self.dim):
            freq1 = 3.0 * (1 + 0.2 * np.sin(0.5 * i))
            freq2 = 4.0 * (1 + 0.15 * np.cos(0.3 * i))
            result += 7 * np.sin(freq1 * np.pi * x[i]) * np.cos(freq2 * np.pi * x[i]) * np.exp(-0.01 * np.abs(x[i]))
        
        # Add a more complex interaction term with stronger coupling and chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased cross-interaction range
                coupling_strength = 4.0 * (1 + 0.3 * np.sin(0.4 * (i + j)))
                result += coupling_strength * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.03 * (x[i] - x[j])**2) * np.sin(2.0 * np.pi * (x[i] + x[j]))
        
        # Add a global shaping term with higher-order polynomial and chaotic perturbation
        result += 0.03 * np.sum(np.abs(x)**4.0) * (1 + 0.2 * np.sin(0.7 * np.sum(x)))
        
        # Add a noise-like component for added complexity with dynamic frequency
        for i in range(self.dim):
            freq = 15.0 * (1 + 0.1 * np.sin(0.3 * i))
            result += 0.8 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Add boundary penalty with exponential scaling
        penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.5 or x[i] > 4.5:
                penalty += 10 * np.exp(2.0 * np.abs(x[i] - np.clip(x[i], -4.5, 4.5)))
        result += penalty
        
        return result