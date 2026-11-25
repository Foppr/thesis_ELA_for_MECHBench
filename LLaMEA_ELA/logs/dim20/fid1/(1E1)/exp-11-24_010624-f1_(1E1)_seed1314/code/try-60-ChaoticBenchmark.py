import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with fractal-like complexity
        self.chaos_params = np.array([3.5 + 0.3 * np.sin(i * 1.2) + 0.1 * np.cos(i * 0.8) + 0.05 * np.sin(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with complex radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with complex coupling
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2) * np.cos(0.3 * x[i])
            # Add fractal-like radial component with multiple frequencies
            radial_term = 0.4 * x[i]**3 * np.sin(0.7 * x[i]) * np.exp(-0.05 * x[i]**2)
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with dynamic frequency modulation and complex phase
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.cos(3 * x[i]) * np.sin(0.5 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with fractal strength and complex interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling strength based on distance and angle between variables
                dist = np.sqrt((x[i] - x[j])**2 + (x[i] + x[j])**2)
                angle = np.arctan2(x[j], x[i])
                coupling_strength = np.exp(-0.03 * dist**2) * (1 + 0.2 * np.sin(angle * 5))
                result += coupling_strength * np.sin(x[i] * x[j] * 0.5) * np.cos(i - j) * np.sin(0.2 * (i + j))
                
        # Add global scaling with fractal frequency components and complex modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.5 * dist_from_origin) * np.cos(0.9 * dist_from_origin) * np.exp(-0.02 * dist_from_origin))
        
        # Add complex noise component with fractal characteristics
        noise = 0.02 * np.sum(np.sin(x * 15) * np.cos(x * 7))
        result += noise
        
        # Add a novel fractal-like term based on iterated complex mappings
        fractal_term = 0.03 * np.sum(np.sin(2 * x + np.cos(x)) * np.cos(3 * x - np.sin(x)))
        result += fractal_term
        
        return result