import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with altered variation pattern
        self.chaos_params = np.array([3.9 + 0.15 * np.sin(i * 0.8) + 0.08 * np.cos(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2)
            # Add radial component with sinusoidal modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.6 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with altered frequency modulation
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.cos(1.5 * x[i]) * np.exp(-0.12 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with modified strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with different exponent
                coupling_strength = np.exp(-0.08 * ((x[i] - x[j])**2 + (x[i] + x[j])**2))
                result += coupling_strength * np.sin(1.5 * x[i] * x[j]) * np.cos(0.5 * (i - j))
                
        # Add global scaling with different frequency components
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin))
        
        # Add noise component to increase irregularity
        noise = 0.015 * np.sum(np.sin(x * 12))
        result += noise
        
        return result