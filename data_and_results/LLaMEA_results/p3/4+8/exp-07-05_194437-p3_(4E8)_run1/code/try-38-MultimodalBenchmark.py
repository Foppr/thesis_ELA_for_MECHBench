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
            result += 5 * np.sin(freq1 * np.pi * x[i]) * np.cos(freq2 * np.pi * x[i])
        
        # Add chaotic cross-interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x[i] - x[j])
                coupling = np.exp(-0.1 * dist) * np.sin(5 * dist)
                result += 2.5 * np.sin(x[i]) * np.cos(x[j]) * coupling
        
        # Add a global shaping term with dynamic exponent
        exp_factor = 1.5 + 0.5 * np.sin(0.2 * self.dim)
        result += 0.03 * np.sum(np.abs(x)**exp_factor)
        
        # Add a noise-like component with dynamic frequency
        for i in range(self.dim):
            freq = 10 + 2 * np.sin(0.1 * i)
            result += 0.8 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2)
        
        # Add a chaotic perturbation term
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(100 * x[i]) * np.cos(50 * x[i])
        result += 0.5 * chaotic_term
        
        return result