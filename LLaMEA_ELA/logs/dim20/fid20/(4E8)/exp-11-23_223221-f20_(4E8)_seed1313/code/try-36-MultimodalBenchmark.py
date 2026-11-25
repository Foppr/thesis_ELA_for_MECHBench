import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis functions with varying widths
        rbf_sum = 0.0
        for i in range(self.dim):
            width = 1.5 + 0.3 * np.sin(i)  # Slightly different widths
            rbf_sum += np.exp(-width * (x[i] - 1.5)**2) + np.exp(-width * (x[i] + 1.5)**2)
        
        # Enhanced cosine modulation with higher frequency
        cos_modulation = 0.0
        for i in range(self.dim):
            cos_modulation += np.cos(3.0 * np.pi * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Quadratic basin term to encourage convergence to origin
        quadratic = 0.07 * np.sum(x**2)
        
        # Cross-terms for increased complexity and interaction between dimensions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.03 * np.sin(3.0 * x[i]) * np.cos(3.0 * x[j])
        
        # Additional nonlinear term to increase landscape complexity
        nonlinear_term = 0.01 * np.sum(np.sin(x)**3)
        
        return rbf_sum + cos_modulation + quadratic + cross_terms + nonlinear_term