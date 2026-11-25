import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Exponential decay terms to create rugged landscape
        for i in range(self.dim):
            f_val += np.exp(-0.1 * x[i]**2) * np.sin(2 * np.pi * x[i])
            
        # Trigonometric oscillations with varying frequencies
        for i in range(self.dim):
            f_val += 0.5 * np.cos(4 * x[i]) * np.sin(3 * x[i])
            
        # Polynomial penalty terms to encourage convergence to origin
        f_val += 0.1 * np.sum(x**6)
        
        # Cross-terms to increase conditioning difficulty
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * x[i] * x[j] * np.sin(0.5 * (x[i]**2 + x[j]**2))
                
        return f_val