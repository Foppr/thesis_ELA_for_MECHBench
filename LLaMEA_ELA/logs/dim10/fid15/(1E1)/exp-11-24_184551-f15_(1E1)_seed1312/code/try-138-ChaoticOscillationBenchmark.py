import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Normalize input to [-1, 1] for chaotic behavior
        x_norm = x / 5.0
        
        # Radial basin term - pulls towards origin
        radial_term = np.sum(x_norm**2) * 0.5
        
        # Sinusoidal oscillation terms - creates multiple local minima
        oscillation_term = 0.0
        for i in range(self.dim):
            oscillation_term += np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            
        # Cross-terms creating non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x_norm[i] * x_norm[j] * np.sin(np.pi * (x_norm[i] + x_norm[j]))
                
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i])
            
        # Combine all terms with different weights
        result = radial_term + 2.0 * oscillation_term + 0.5 * cross_term + 0.3 * chaotic_term
        
        # Add small random noise for robustness
        noise = np.random.normal(0, 0.01)
        
        return result + noise