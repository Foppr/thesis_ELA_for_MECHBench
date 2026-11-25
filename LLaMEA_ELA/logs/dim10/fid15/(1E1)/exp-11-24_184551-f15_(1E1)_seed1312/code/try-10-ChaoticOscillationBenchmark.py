import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add sinusoidal oscillations with varying frequencies
        for i in range(self.dim):
            # Use each dimension in a unique way to create complexity
            result += np.sin(x[i]) * np.cos(2 * x[i]) * np.sin(3 * x[i])
            
        # Add exponential barrier terms that make optimization difficult
        barrier_term = 0.0
        for i in range(self.dim):
            # Create steep barriers near the boundaries
            barrier_term += np.exp(-10 * (x[i] - 5.0)**2) + np.exp(-10 * (x[i] + 5.0)**2)
            
        # Add coupling terms between dimensions to create interdependence
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(x[i] * x[j]) * 0.1
                
        # Add a quadratic term to ensure the function is bounded below
        quadratic_term = 0.5 * np.sum(x**2)
        
        # Combine all terms with different weights
        result = result * 2.0 - barrier_term * 0.5 + coupling_term * 3.0 + quadratic_term * 0.1
        
        return result