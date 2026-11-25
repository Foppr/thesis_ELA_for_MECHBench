import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with enhanced complexity
        self.chaos_params = np.array([3.8 + 0.15 * np.sin(i * 0.7) + 0.08 * np.cos(i * 0.3) + 0.03 * np.sin(i * 0.1) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic logistic map component with multi-scale radial symmetry
        for i in range(self.dim):
            # Apply modified logistic map dynamics with enhanced nonlinearity
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2) * np.cos(0.5 * x[i])
            # Add multi-scale radial component with different frequencies
            radial_term = 0.4 * x[i]**2 * np.sin(0.3 * x[i]) + 0.2 * x[i]**3 * np.cos(0.7 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with adaptive frequency modulation
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.sin(1.5 * x[i]) * np.exp(-0.08 * np.abs(x[i]))
            result += poly_term
            
        # Add enhanced cross-dimensional coupling with adaptive strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on variable interactions
                coupling_strength = np.exp(-0.03 * ((x[i] - x[j])**2 + 0.5 * (x[i] + x[j])**2)) * (1 + 0.2 * np.sin(i * j))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(0.5 * (i - j)) * np.exp(-0.1 * np.abs(x[i] - x[j]))
                
        # Add global scaling with multi-frequency components
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.6 * dist_from_origin) * np.exp(-0.05 * dist_from_origin))
        
        # Add enhanced noise component for increased irregularity
        noise = 0.015 * np.sum(np.sin(x * 12) + 0.5 * np.cos(x * 8))
        result += noise
        
        return result