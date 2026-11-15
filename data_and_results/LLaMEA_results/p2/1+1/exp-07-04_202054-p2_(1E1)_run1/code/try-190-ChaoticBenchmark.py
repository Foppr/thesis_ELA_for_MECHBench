import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_value = np.sum(x**2)
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_value += 1.5 * np.sin(10 * np.exp(x[i])) * np.cos(5 * np.exp(-x[i]))
            
        # Exponential polynomial interactions
        for i in range(self.dim):
            f_value += 0.8 * np.exp(0.5 * x[i]**3) * np.sin(x[i])
            
        # Asymmetric cross-variable interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.6 * np.sin(3 * x[i]) * np.exp(-0.5 * x[j]**2) * np.cos(2 * x[i] + x[j])
                
        # Multi-scale chaotic modulation
        f_value += 0.7 * np.sum(np.sin(np.exp(x)) * np.cos(np.exp(-x)))
        
        # Higher-order polynomial with exponential modulation
        for i in range(self.dim):
            f_value += 0.5 * x[i]**5 * np.exp(-0.1 * np.abs(x[i]))
            
        # Asymmetric exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.4 * np.exp(-0.5 * x[i]**2) * np.sin(2 * x[j]) * np.cos(x[i] + x[j])
                
        # Chaotic sine-cosine combinations
        f_value += 0.6 * np.sum(np.sin(2 * np.exp(x)) * np.cos(3 * np.exp(-x)) * np.sin(4 * x))
        
        # Mixed polynomial and exponential terms
        for i in range(self.dim):
            f_value += 0.3 * x[i]**4 * np.exp(-0.2 * x[i]**2)
            
        # Asymmetric variable coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.5 * np.sin(4 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.3 * np.abs(x[i] - x[j]))
                
        # Additional chaotic component with logarithmic modulation
        f_value += 0.4 * np.sum(np.sin(x) * np.cos(np.log(np.abs(x) + 1)) * np.exp(-0.1 * x**2))
        
        # Increased complexity in exponential polynomial interactions
        for i in range(self.dim):
            f_value += 0.35 * x[i]**6 * np.exp(-0.05 * x[i]**3)
            
        # Multi-modal exponential interactions
        for i in range(self.dim):
            f_value += 0.25 * np.exp(2 * np.sin(x[i])) * np.cos(1.5 * x[i])
            
        # Asymmetric cross-variable exponential terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.3 * np.exp(-x[i]**2) * np.sin(2 * x[j]) * np.cos(1.5 * x[i] + 0.5 * x[j])
                
        return f_value