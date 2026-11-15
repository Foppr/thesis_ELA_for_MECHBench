import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic sine wave components with varying amplitudes and frequencies
        for i in range(self.dim):
            f_val += 0.2 * np.sin(13 * x[i]) * np.cos(9 * x[i]) * np.sin(5 * x[i])
            
        # Radial basis function components with random centers and varying widths
        centers = np.random.uniform(-5, 5, self.dim)
        for i in range(self.dim):
            f_val += 0.15 * np.exp(-0.5 * ((x[i] - centers[i]) / 1.5)**2)
            
        # Asymmetric polynomial interactions
        for i in range(self.dim):
            f_val += 0.05 * (x[i]**5) * np.sin(x[i]) + 0.03 * (x[i]**3) * np.cos(x[i])
            
        # Cross-term interactions with non-uniform coefficients
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-interaction
                f_val += 0.02 * np.sin(2 * x[i]) * np.cos(3 * x[j]) * (x[i]**2 + x[j]**2)
                
        # Add a set of scattered local minima using a modified Ackley-like function
        f_val += 0.1 * np.exp(-0.2 * np.sqrt(np.sum(x**2))) + 0.1 * np.cos(5 * np.sqrt(np.sum(x**2))) + 1.0
        
        return f_val