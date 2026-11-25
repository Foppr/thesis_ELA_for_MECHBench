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
            width = 1.0 + 0.5 * np.sin(i)  # Varying widths
            rbf_sum += np.exp(-width * (x[i] - 1.0)**2) + np.exp(-width * (x[i] + 1.0)**2)
        
        # Cosine modulation to create multiple local minima
        cosine_mod = 0.0
        for i in range(self.dim):
            cosine_mod += np.cos(2.0 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-terms with different frequencies
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.1 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[j])
        
        # Quadratic basin term to ensure global minimum at origin
        quadratic = 0.05 * np.sum(x**2)
        
        return rbf_sum + cosine_mod + cross_terms + quadratic