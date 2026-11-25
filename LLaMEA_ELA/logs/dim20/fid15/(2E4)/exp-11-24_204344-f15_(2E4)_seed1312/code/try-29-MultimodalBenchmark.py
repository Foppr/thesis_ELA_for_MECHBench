import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Base quadratic term
        quadratic = np.sum(x**2) / self.dim
        
        # Chaotic sine wave component with varying frequencies and amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 3.0 * np.sin(7 * x[i] + np.sin(3 * x[i])) ** 2 + 1.5 * np.cos(4 * x[i] + np.cos(2 * x[i])) ** 2
        
        # Radial basin term with non-uniform scaling
        radial_basin = 0.1 * np.sum((x**2 - 2.0)**2)
        
        # Add a multi-modal noise component using logistic map
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(11 * x[i]) * np.cos(9 * x[i])
        
        # Saddle point with higher-order polynomial terms
        saddle = 0.05 * np.sum(x**6)
        
        # Cross-dimensional coupling with interaction coefficients
        cross_interaction = 0.08 * np.sum((x[:-1] + x[1:])**2)
        
        return quadratic + chaotic + radial_basin + noise + saddle + cross_interaction