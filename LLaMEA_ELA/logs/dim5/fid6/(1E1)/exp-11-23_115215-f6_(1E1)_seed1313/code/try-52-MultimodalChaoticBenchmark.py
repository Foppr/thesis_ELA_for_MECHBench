import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for wave interference
        self.freqs = np.linspace(1.0, 10.0, dim)
        # Precompute decay rates
        self.decay_rates = np.linspace(0.1, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2) * 0.1
        
        # Add exponential decay components with sinusoidal modulation
        for i in range(self.dim):
            f_val += np.exp(-self.decay_rates[i] * np.abs(x[i])) * np.sin(self.freqs[i] * x[i])
            
        # Add trigonometric wave interference patterns
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                f_val += 0.2 * np.sin(self.freqs[i] * x[i]) * np.cos(self.freqs[j] * x[j])
                
        # Add gradient-based attraction fields (local minima)
        for i in range(self.dim):
            center = 3.0 * np.sin(i * 0.7)
            f_val += 0.5 * np.exp(-0.5 * ((x[i] - center) / 1.5)**2)
            
        # Add higher-order polynomial interactions
        for i in range(self.dim):
            f_val += 0.05 * x[i]**4 + 0.03 * x[i]**6
            
        # Add multi-scale sinusoidal modulations
        for i in range(self.dim):
            f_val += 0.3 * np.sin(2 * x[i]) + 0.2 * np.sin(5 * x[i]) + 0.1 * np.sin(10 * x[i])
            
        # Add asymmetric coupling with exponential weights
        for i in range(1, self.dim):
            weight = np.exp(-0.2 * i)
            f_val += weight * (x[i] - x[i-1])**2 + 0.05 * np.abs(x[i] - x[i-1])**1.7
            
        # Add a complex non-linear transformation
        f_val += 0.1 * np.sin(np.sum(np.exp(-x**2))) + 0.05 * np.cos(np.prod(x))
        
        return f_val