import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Sinusoidal oscillation component - creates many local minima
        for i in range(self.dim):
            result += np.sin(5.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Radial basin term - pulls solutions toward origin
        radial_term = 0.5 * np.sum(x**2)
        
        # Cross-terms creating non-separability and complex interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(0.5 * (x[i]**2 + x[j]**2))
                
        # Add a chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10.0 * np.abs(x[i])) * np.cos(3.0 * x[i])
            
        # Combine all terms with different weights
        result = result + radial_term + cross_term * 0.1 + chaotic * 0.05
        
        return result