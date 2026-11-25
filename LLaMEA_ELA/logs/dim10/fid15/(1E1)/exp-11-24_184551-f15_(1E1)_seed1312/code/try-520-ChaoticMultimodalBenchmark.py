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
        radial_basin = 0.5 * np.sum(x_norm**2)
        
        # Sinusoidal oscillation terms creating multiple local minima
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(10 * x_norm[i]) * np.cos(5 * x_norm[i])
            
        # Cross-terms creating non-separability and complex interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x_norm[i] * x_norm[j] * np.sin(x_norm[i] + x_norm[j])
                
        # Chaotic component with exponential growth
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.exp(-x_norm[i]**2) * np.sin(20 * x_norm[i])**2
            
        # Combine all terms with different weights
        result = radial_basin - 0.5 * sinusoidal + 0.1 * cross_term + 0.3 * chaotic
        
        # Add small noise for robustness
        noise = 0.001 * np.sum(np.random.randn(self.dim))
        
        return result + noise