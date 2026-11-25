import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basin term - pulls toward origin
        radial_basin = 0.5 * np.sum(x_norm**2)
        
        # Sinusoidal oscillation terms - create many local minima
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(5.0 * x_norm[i]) * np.cos(3.0 * x_norm[i])
            
        # Cross-term interactions - create complex curvature
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x_norm[i] * x_norm[j] * np.sin(x_norm[i] + x_norm[j])
                
        # Chaotic component - small perturbations to increase difficulty
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10.0 * x_norm[i]) * np.exp(-x_norm[i]**2)
            
        # Combine all terms with different weights
        result = radial_basin - 0.3 * oscillation + 0.1 * cross_term + 0.05 * chaotic
        
        return result