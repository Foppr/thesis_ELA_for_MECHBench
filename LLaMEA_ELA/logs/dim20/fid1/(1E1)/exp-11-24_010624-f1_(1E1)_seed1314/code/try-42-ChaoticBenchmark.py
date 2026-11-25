import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with enhanced complexity
        self.chaos_params = np.array([3.8 + 0.15 * np.sin(i * 0.7) + 0.1 * np.cos(i * 0.3) + 0.05 * np.sin(i * 0.1) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic logistic map component with adaptive radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply enhanced logistic map dynamics with variable parameter
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2)
            # Add adaptive radial component with multi-frequency sinusoidal modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.5 * x[i]) * np.cos(0.2 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with adaptive frequency modulation and multi-scale components
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.cos(1.5 * x[i]) * np.exp(-0.15 * np.abs(x[i])) + \
                       0.03 * x[i]**4 * np.sin(0.8 * x[i]) * np.exp(-0.05 * x[i]**2)
            result += poly_term
            
        # Add cross-dimensional coupling with adaptive strength and multi-scale interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on both variables with dynamic scaling
                coupling_strength = np.exp(-0.03 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * \
                                   (1 + 0.2 * np.sin(0.5 * (x[i] + x[j])))
                # Multi-scale interaction terms
                interaction = coupling_strength * (np.sin(x[i] * x[j]) * np.cos(i - j) + 
                                                  0.3 * np.cos(x[i] * x[j]) * np.sin(i + j))
                result += interaction
                
        # Add global scaling with multi-frequency components and adaptive modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.3 * dist_from_origin) * np.cos(0.7 * dist_from_origin) + 
                  0.1 * np.sin(1.2 * dist_from_origin))
        
        # Add enhanced noise component with multi-scale frequency
        noise = 0.015 * np.sum(np.sin(x * 15) + 0.5 * np.cos(x * 8))
        result += noise
        
        return result