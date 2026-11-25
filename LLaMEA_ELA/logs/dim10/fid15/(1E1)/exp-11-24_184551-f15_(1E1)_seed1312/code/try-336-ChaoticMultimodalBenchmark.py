import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Radial basin term - pulls solutions toward origin
        radial_term = 0.5 * np.sum(x**2)
        
        # Sinusoidal oscillation terms - create complex multimodal structure
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-terms creating interaction between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * np.sin(x[i])) * np.cos(7.0 * x[i])
            
        # Combine all terms with different weights
        result = radial_term + 2.0 * sin_term + 0.5 * cross_term + 0.3 * chaotic_term
        
        # Add small noise to make it non-trivial
        noise = np.random.normal(0, 0.01)
        
        return result + noise