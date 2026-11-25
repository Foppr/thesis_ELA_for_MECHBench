import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Radial basin term - pulls solutions towards origin
        radial_term = 0.5 * np.sum(x**2)
        
        # Sinusoidal oscillation terms - create complex multimodal structure
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-terms creating non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += (x[i]**2 - 1.4) * x[i] * 0.1
            
        # Combine all terms with different weights
        result = radial_term + sin_term + cross_term + chaotic_term
        
        # Add small noise to prevent exact replicability
        noise = np.random.normal(0, 0.001)
        
        return result + noise