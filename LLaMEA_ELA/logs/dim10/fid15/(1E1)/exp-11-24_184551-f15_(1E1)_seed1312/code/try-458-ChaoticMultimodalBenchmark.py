import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basin term - pulls towards origin
        radial_basin = 0.5 * np.sum(x_norm**2)
        
        # Sinusoidal oscillation terms creating multiple local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x_norm[i]) * np.cos(3.0 * x_norm[i])
            
        # Cross-terms creating non-separability and complex interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x_norm[i] * x_norm[j]) * 0.1
                
        # Additional chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += (np.sin(2.0 * np.pi * x_norm[i]) + 
                           0.5 * np.sin(4.0 * np.pi * x_norm[i]))
        
        # Combine all terms with different weights
        result = radial_basin - sin_term - cross_term - chaotic_term
        
        # Add small noise for non-triviality
        noise = 0.01 * np.sum(np.random.randn(self.dim) * x_norm)
        
        return result + noise