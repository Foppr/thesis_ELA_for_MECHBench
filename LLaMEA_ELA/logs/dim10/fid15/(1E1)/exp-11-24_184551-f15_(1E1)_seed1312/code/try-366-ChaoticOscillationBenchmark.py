import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Normalize input to [-1, 1] range for stable oscillations
        x_norm = x / 5.0
        
        # Radial basin term - pulls solutions toward origin
        radial_term = np.sum(x_norm**2) * 0.5
        
        # Sinusoidal oscillation terms with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x_norm[i]) * np.cos(3.0 * x_norm[i])
            
        # Cross-terms creating complex interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_norm[i] * x_norm[j]) * np.sin(x_norm[i] + x_norm[j])
                
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * np.sin(x_norm[i])) * 0.3
            
        # Combine all terms with different weights
        result = radial_term - sin_term + cross_term + chaotic_term
        
        # Add small noise to prevent trivial solutions
        noise = np.random.normal(0, 0.01)
        
        return result + noise