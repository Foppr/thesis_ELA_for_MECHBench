import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with fractional scaling
        f_val = np.sum(x**2.5)
        
        # Add chaotic sinusoidal perturbations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(13 * x[i]) * np.cos(9 * x[i]) * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add fractional polynomial coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * (x[i]**1.7) * (x[j]**2.3) * np.sin(8 * (x[i] + x[j]))
                
        # Add a complex global minimum structure with exponential modulation
        f_val += 0.2 * np.sum(np.exp(-0.5 * x**2) * np.sin(20 * x) * np.cos(15 * x))
        
        # Add chaotic cross-dimensional interactions with varying amplitude
        f_val += 0.15 * np.sum(np.sin(10 * x) * np.cos(7 * x) * np.sin(3 * x) * np.cos(x))
        
        # Add a fractal-like component with recursive sinusoidal modulation
        f_val += 0.08 * np.sum(np.sin(25 * x) * np.cos(18 * x) * np.sin(12 * x) * np.cos(6 * x))
        
        return f_val