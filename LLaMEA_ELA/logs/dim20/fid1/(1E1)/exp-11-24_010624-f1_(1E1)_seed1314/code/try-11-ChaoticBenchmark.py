import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map coefficients for chaos generation
        self.logistic_coeffs = np.array([3.9 * np.sin(i * 0.5) + 0.1 for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with radial symmetry
        for i in range(self.dim):
            # Apply logistic map dynamics with varying parameter
            chaotic_val = self.logistic_coeffs[i] * x[i] * (1 - x[i])
            # Add radial component to create basin structure
            radial_term = 0.5 * x[i]**2
            result += chaotic_val + radial_term
            
        # Add polynomial interpolation terms for smooth transitions
        for i in range(self.dim):
            # Use higher-order polynomial with sinusoidal modulation
            poly_term = 0.1 * x[i]**4 * np.cos(3 * x[i])
            result += poly_term
            
        # Add cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = np.exp(-0.1 * np.sqrt((x[i] - x[j])**2 + 1e-8))
                result += coupling_strength * np.sin(x[i] * x[j]) * (1 + 0.1 * np.sin(i + j))
                
        # Add a global scaling factor based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(dist_from_origin))
        
        return result