import numpy as np

class ChaoticMultiScaleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add polynomial basin term (central attraction)
        poly_basin = np.sum(x**4) * 0.01
        
        # Add chaotic sinusoidal components with varying frequencies
        for i in range(self.dim):
            # High frequency oscillations
            result += np.sin(10.0 * x[i]) * np.cos(5.0 * x[i])
            # Medium frequency
            result += 0.5 * np.sin(3.0 * x[i]**2) * np.cos(2.0 * x[i])
            # Low frequency
            result += 0.3 * np.sin(0.5 * x[i]) * np.cos(0.2 * x[i]**3)
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Add a quadratic penalty for out-of-bounds regions
        bounds_penalty = 0.0
        for i in range(self.dim):
            if x[i] < -5.0 or x[i] > 5.0:
                bounds_penalty += (abs(x[i]) - 5.0)**2
                
        # Combine all terms
        return poly_basin + result + bounds_penalty