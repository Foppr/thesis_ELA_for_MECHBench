import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += np.sin(2 * np.pi * x[i]) * np.cos(3 * x[i])
            
        # Exponential decay terms to create rugged landscape
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-0.05 * x[i]**2) * np.sin(5 * x[i])
            
        # Cross-dimensional interactions with varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(x[i] + x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
                
        # Polynomial penalty terms with mixed conditioning
        f_val += 0.05 * np.sum(x**4) + 0.02 * np.sum(x**8)
        
        # Additional cross-term to increase conditioning difficulty
        for i in range(self.dim):
            f_val += 0.3 * x[i] * np.sin(0.1 * np.sum(x**2))
                
        return f_val