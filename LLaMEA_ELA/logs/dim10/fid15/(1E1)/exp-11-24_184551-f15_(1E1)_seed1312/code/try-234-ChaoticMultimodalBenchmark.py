import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basin term - pulls solutions toward origin
        radial_term = 0.5 * np.sum(x_norm**2)
        
        # Sinusoidal oscillation terms creating multiple local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            
        # Cross-terms creating non-separability and complex interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_norm[i] * x_norm[j]) * np.sin(np.pi * (x_norm[i] + x_norm[j]))
                
        # Additional chaotic component with exponential scaling
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.exp(-2 * x_norm[i]**2) * np.sin(10 * np.pi * x_norm[i])
            
        # Combine all terms with different weights
        result = radial_term - 0.3 * sin_term + 0.1 * cross_term + 0.2 * chaotic_term
        
        # Add small random noise for robustness
        noise = 0.001 * np.random.rand()
        
        return result + noise