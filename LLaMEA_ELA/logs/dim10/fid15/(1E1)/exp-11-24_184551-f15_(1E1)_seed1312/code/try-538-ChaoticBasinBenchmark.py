import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        f_val = 0.0
        
        # Radial basin term - encourages convergence to origin
        radial_term = np.sum(x**2) * 0.05
        
        # Sinusoidal oscillation terms - create chaotic landscape
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-terms creating non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Add chaotic component with varying frequency
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * x[i]**2) * np.cos(7.0 * x[i])
            
        # Combine all terms
        f_val = radial_term + sin_term + cross_term + chaotic_term
        
        # Add small noise to prevent trivial solutions
        noise = 0.01 * np.sum(np.random.randn(self.dim))
        
        return f_val + noise