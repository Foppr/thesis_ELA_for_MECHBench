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
        result += 0.1 * np.sum(x**2)
        
        # Add chaotic periodic terms with dynamic frequencies
        for i in range(self.dim):
            freq1 = 2 * np.pi * (1 + 0.5 * np.sin(0.1 * i))
            freq2 = 3 * np.pi * (1 + 0.3 * np.cos(0.15 * i))
            result += 5 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
        
        # Add exponential interaction terms with dynamic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased cross-interaction
                coupling = np.exp(-0.1 * (x[i] - x[j])**2) * (1 + 0.2 * np.sin(0.5 * (x[i] + x[j])))
                result += 3 * np.sin(x[i]) * np.cos(x[j]) * coupling
        
        # Add a global shaping term with adaptive exponents
        result += 0.02 * np.sum(np.abs(x)**(2.5 + 0.5 * np.sin(0.2 * np.arange(self.dim))))
        
        # Add a noise-like component with chaotic modulation
        for i in range(self.dim):
            modulation = 1 + 0.3 * np.sin(0.7 * i) * np.cos(0.4 * i)
            result += 0.8 * np.sin(modulation * 15 * x[i]) * np.cos(modulation * 8 * x[i])
        
        # Add a dynamic conditioning term that varies with dimension
        dynamic_cond = 1 + 0.1 * np.sin(0.3 * self.dim)
        result *= dynamic_cond
        
        # Add a chaotic perturbation term
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += np.sin(100 * x[i] + i) * np.cos(75 * x[i] - i)
        result += 0.05 * chaotic_sum**2
        
        return result