import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Radial basin term - encourages convergence to origin
        radial_basin = 0.5 * np.sum(x**2)
        
        # Sinusoidal oscillation terms - create many local minima
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-terms creating interaction between dimensions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j]))
                
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(x[i]**2) * np.cos(x[(i+1) % self.dim]**2)
            
        # Add a small noise term to make it non-trivial
        noise = 0.01 * np.sum(np.random.randn(self.dim))
        
        return radial_basin + sinusoidal + cross_terms + chaotic + noise