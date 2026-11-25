import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Enhanced sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += np.sin(3 * np.pi * x[i]) * np.cos(2 * x[i]) + 0.5 * np.sin(5 * x[i])
            
        # Improved exponential decay terms to create rugged landscape
        for i in range(self.dim):
            f_val += 0.7 * np.exp(-0.1 * x[i]**2) * np.sin(4 * x[i]) + 0.3 * np.exp(-0.05 * x[i]**2)
            
        # Enhanced cross-dimensional interactions with stronger conditioning
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.sin(x[i] + x[j]) * np.cos(0.3 * (x[i]**2 + x[j]**2)) + 0.1 * np.sin(2 * (x[i] - x[j]))
                
        # Modified polynomial penalty terms with mixed conditioning
        f_val += 0.08 * np.sum(x**4) + 0.05 * np.sum(x**6) + 0.03 * np.sum(x**8)
        
        # Additional cross-term to increase conditioning difficulty and create more complex landscape
        for i in range(self.dim):
            f_val += 0.4 * x[i] * np.sin(0.2 * np.sum(x**2)) + 0.2 * np.cos(0.1 * np.sum(x**3))
                
        return f_val