import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Polynomial basin term - creates a smooth central attraction
        basin_term = 0.1 * np.sum(x**4)
        
        # Sinusoidal multimodal terms - creates many local minima
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += np.sin(5.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Cross-terms creating non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * (i + j) / (self.dim * (self.dim - 1) / 2)
                
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(100.0 * np.sin(x[i])) * np.cos(0.5 * x[i])
            
        # Combine all terms with different weights
        return basin_term + modal_term + cross_term + chaotic_term