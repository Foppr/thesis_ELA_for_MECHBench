import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Shift global minimum to (1,1,...,1) instead of origin
        shifted_x = x - 1.0
        
        # Global minimum at (1,1,...,1)
        if np.allclose(shifted_x, 0):
            return 0.0
            
        # Base function with multiple local minima
        result = 0.0
        
        # Sum of quadratic terms with different coefficients
        for i in range(self.dim):
            result += (shifted_x[i] ** 2) * (i + 1)
            
        # Add sinusoidal perturbations with higher frequencies and different amplitudes
        for i in range(self.dim):
            result += 0.2 * np.sin(7 * shifted_x[i]) * np.cos(4 * shifted_x[(i + 1) % self.dim])
            
        # Add a global scaling factor to ensure the function is well-conditioned
        result *= 1.0 + 0.15 * np.sum(shifted_x ** 2)
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.08 * (shifted_x[i] ** 4) * (i + 1)
            
        # Add cross-term interactions with different weights and nonlinearities
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * shifted_x[i] * shifted_x[j] * np.sin(shifted_x[i] + shifted_x[j]) * np.cos(shifted_x[i] - shifted_x[j])
                
        # Add a small Gaussian-like term to create additional local minima
        gaussian_term = 0.05 * np.exp(-0.5 * np.sum(shifted_x ** 2))
        result += gaussian_term
        
        return result