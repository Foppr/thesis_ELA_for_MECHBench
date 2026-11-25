import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with fractal-like complexity
        self.chaos_params = np.array([3.5 + 0.8 * np.sin(i * 1.2 + np.cos(i * 0.5)) + 
                                      0.3 * np.sin(i * 0.3 + np.cos(i * 0.7)) * np.cos(i * 0.4) 
                                      for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Nested chaotic logistic map component with fractal interpolation
        for i in range(self.dim):
            # Apply nested logistic maps with dynamic parameters
            val1 = self.chaos_params[i] * x[i] * (1 - x[i]**2)
            val2 = 3.9 * val1 * (1 - val1**2)  # Nested map
            chaotic_val = val2 + 0.1 * np.sin(val1 * 5) * np.cos(x[i] * 2)
            result += chaotic_val
            
        # Add multi-scale radial symmetry with fractal modulation
        for i in range(self.dim):
            radial_term = 0.2 * x[i]**3 * np.sin(0.4 * x[i]) * np.cos(0.2 * x[i]**2)
            result += radial_term
            
        # Add higher-order polynomial terms with adaptive frequency modulation
        for i in range(self.dim):
            freq_mod = 1 + 0.5 * np.sin(i * 0.6) * np.cos(i * 0.3)
            poly_term = 0.08 * x[i]**6 * np.exp(-0.1 * np.abs(x[i])) * np.sin(freq_mod * x[i])
            result += poly_term
            
        # Add cross-dimensional coupling with fractal strength and multi-scale interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Limited but complex coupling
                # Fractal-like coupling strength
                coupling_strength = np.exp(-0.03 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * \
                                   (1 + 0.2 * np.sin(i * j * 0.5))
                interaction = coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j)
                result += interaction
                
        # Add global scaling with multi-fractal components
        dist_from_origin = np.sqrt(np.sum(x**2))
        fractal_factor = (1 + 0.2 * np.sin(0.5 * dist_from_origin) * 
                         np.cos(0.3 * dist_from_origin) * 
                         np.sin(0.7 * dist_from_origin))
        result *= fractal_factor
        
        # Add adaptive noise with chaotic modulation
        noise = 0.02 * np.sum(np.sin(x * 15 + np.cos(x * 0.5)) * np.exp(-0.05 * np.abs(x)))
        result += noise
        
        # Add a small but complex bias term to ensure global minimum is not trivial
        bias = 0.05 * np.sum(np.sin(x * 3) * np.cos(x * 1.5))
        result += bias
        
        return result