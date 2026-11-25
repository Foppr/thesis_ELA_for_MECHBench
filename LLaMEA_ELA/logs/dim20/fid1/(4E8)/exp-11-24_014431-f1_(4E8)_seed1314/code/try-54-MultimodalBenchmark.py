import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Polynomial oscillations with varying degrees and scales
        for i in range(self.dim):
            f_val += np.sin(3 * x[i]) * (x[i]**2) + 0.5 * np.cos(4 * x[i]) * (x[i]**3)
            
        # Radial basis function interactions with multi-scale decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x[i] - x[j])**2 + 0.1)
                f_val += 0.3 * np.exp(-distance**2) * np.sin(2 * np.pi * (x[i] + x[j]))
                
        # Multi-scale conditioning with varying penalty strengths
        for i in range(self.dim):
            f_val += 0.2 * (x[i]**4) * np.cos(0.5 * x[i]) + 0.1 * (x[i]**6) * np.sin(0.3 * x[i])
            
        # Cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * (x[i] * x[j])**2 * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Additional harmonic terms with varying frequencies
        for i in range(self.dim):
            f_val += 0.4 * np.sin(6 * x[i]) * np.cos(2 * x[i]) + 0.3 * np.sin(8 * x[i])
            
        # Global conditioning term
        f_val += 0.01 * np.sum(x**10) + 0.005 * np.sum(x**12)
        
        return f_val