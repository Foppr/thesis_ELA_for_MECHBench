import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Polynomial basin term - creates a smooth central attraction
        basin_term = 0.5 * np.sum(x**4) / self.dim
        
        # Sinusoidal oscillation terms - create many local minima
        oscillation_term = 0.0
        for i in range(self.dim):
            oscillation_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-terms between dimensions - create non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Chaotic component - small perturbations that make it hard to predict
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += 0.05 * np.sin(100.0 * x[i]) * np.cos(75.0 * x[i])
            
        # Combine all terms
        return basin_term + oscillation_term + cross_term + chaotic_term