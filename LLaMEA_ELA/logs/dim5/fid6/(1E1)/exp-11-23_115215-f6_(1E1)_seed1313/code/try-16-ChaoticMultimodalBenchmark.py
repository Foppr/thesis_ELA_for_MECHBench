import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic sine-cosine components with exponential decay
        for i in range(self.dim):
            f_val += np.exp(-0.1 * np.abs(x[i])) * (np.sin(10 * x[i]) + 0.5 * np.cos(15 * x[i]))
            
        # Introduce asymmetric interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                f_val += 0.3 * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
                
        # Add a complex high-frequency component with varying amplitudes
        for i in range(self.dim):
            f_val += 0.4 * np.sin(20 * x[i]) * np.cos(13 * x[i]) * np.sin(7 * x[i])
            
        # Introduce a chaotic term using logistic map-like behavior
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(np.pi * x[i] * np.exp(-x[i]**2))
        f_val += 0.25 * chaos_term
            
        # Add polynomial and exponential interactions
        for i in range(self.dim):
            f_val += 0.1 * x[i]**3 * np.exp(-0.01 * x[i]**2) + 0.05 * np.abs(x[i])**1.5
            
        # Add cross-dimensional exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
                
        # Add a final chaotic correction term
        f_val += 0.03 * np.sum(np.sin(25 * x) * np.cos(18 * x))
        
        return f_val