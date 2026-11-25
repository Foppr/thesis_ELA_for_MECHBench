import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum at origin
        result = np.sum(x**2)
        
        # Add exponentially decaying sinusoidal terms with varying frequencies
        for i in range(self.dim):
            frequency = 2**(i % 3 + 1)  # Varying frequencies: 2, 4, 8
            decay = 0.5**(i // 3 + 1)   # Exponential decay
            result += decay * np.sin(frequency * x[i]) * np.cos(frequency * x[i])
            
        # Add coupled terms with polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling_strength = 0.1 / (1 + abs(i-j))
                result += coupling_strength * (x[i]**3 - x[j]**2) * np.sin(x[i] + x[j])
                
        # Add a complex interaction term that creates many local minima
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(10 * x[i]) * np.cos(7 * x[j]) * (x[i] - x[j])**2
                
        # Add a chaotic component using logistic map-like behavior
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(100 * x[i]) * np.cos(50 * x[i])
        result += 0.02 * chaos_term
        
        return result