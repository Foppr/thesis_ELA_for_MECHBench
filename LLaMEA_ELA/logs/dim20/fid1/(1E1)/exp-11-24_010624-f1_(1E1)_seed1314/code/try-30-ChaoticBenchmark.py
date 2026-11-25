import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with fractal-like complexity
        self.chaos_params = np.array([3.8 + 0.2 * np.sin(i * 1.1) + 0.1 * np.cos(i * 0.5) + 0.05 * np.sin(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with phase shift
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2) + 0.1 * np.sin(x[i] * 3)
            # Add radial component with sinusoidal modulation and dynamic frequency
            radial_term = 0.4 * x[i]**2 * np.sin(0.7 * x[i]) * np.cos(0.2 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation and fractal scaling
        for i in range(self.dim):
            poly_term = 0.1 * x[i]**6 * np.cos(3 * x[i]) * np.exp(-0.2 * np.abs(x[i])) * (1 + 0.1 * np.sin(x[i] * 5))
            result += poly_term
            
        # Add cross-dimensional coupling with fractal strength and phase modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling strength based on both variables
                coupling_strength = np.exp(-0.1 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * (1 + 0.1 * np.sin(x[i] * x[j]))
                phase_mod = np.sin(i * x[j] + j * x[i]) * np.cos(i * j)
                result += coupling_strength * np.sin(x[i] * x[j]) * phase_mod
                
        # Add global scaling with multiple frequency components and fractal modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        fractal_factor = 1 + 0.2 * np.sin(0.5 * dist_from_origin) * np.cos(0.9 * dist_from_origin) * np.sin(0.3 * dist_from_origin)
        result *= fractal_factor
        
        # Add noise component with chaotic frequency modulation to increase irregularity
        noise = 0.02 * np.sum(np.sin(x * 15 + np.sin(x * 7)))
        result += noise
        
        # Add a small perturbation to create multiple local minima
        perturbation = 0.005 * np.sum(np.sin(x * 20) * np.cos(x * 13))
        result += perturbation
        
        return result