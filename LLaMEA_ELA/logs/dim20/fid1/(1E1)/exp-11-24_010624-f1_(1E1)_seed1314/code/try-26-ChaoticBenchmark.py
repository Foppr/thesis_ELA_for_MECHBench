import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly modified chaotic parameters for increased complexity
        self.chaos_params = np.array([3.9 + 0.15 * np.sin(i * 0.8) + 0.08 * np.cos(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with higher nonlinearity
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**3)
            # Add radial component with sinusoidal modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.6 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.cos(2.5 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with dynamic strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Increased coupling strength and different interaction form
                coupling_strength = np.exp(-0.1 * ((x[i] - x[j])**2 + (x[i] + x[j])**2))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(2 * (i - j))
                
        # Add global scaling with multiple frequency components
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin))
        
        # Add noise component to increase irregularity
        noise = 0.015 * np.sum(np.sin(x * 12))
        result += noise
        
        return result