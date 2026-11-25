import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Sinusoidal base term creating complex oscillations
        sin_term = np.sum(np.sin(5.0 * x) * np.exp(-0.1 * x**2))
        
        # Polynomial penalty terms to create multiple local minima
        poly_term = np.sum(x**4 - 10.0 * x**2 + 5.0 * x)
        
        # Additional chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(min(5, self.dim)):
            if i < len(x):
                chaotic_term += np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
        
        # Combine all terms with different weights
        result = -0.5 * sin_term + 0.3 * poly_term + 0.2 * chaotic_term
        
        # Add a global quadratic basin to encourage convergence
        basin = 0.1 * np.sum(x**2)
        
        return result + basin