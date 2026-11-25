import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with fractal-like variation
        self.chaos_params = np.array([3.9 + 0.2 * np.sin(i * 1.1) + 0.1 * np.cos(i * 0.5) + 0.05 * np.sin(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with enhanced radial symmetry and multi-frequency modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with fractional chaos
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2) + 0.1 * np.sin(x[i] * 3)
            # Add enhanced radial component with multi-harmonic modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with dynamic frequency modulation and complex phase shifts
        for i in range(self.dim):
            poly_term = 0.1 * x[i]**6 * np.cos(3 * x[i]) * np.exp(-0.15 * np.abs(x[i])) * np.sin(0.5 * x[i])
            result += poly_term
            
        # Add cross-dimensional coupling with adaptive strength and multi-modal interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with non-linear transformation
                coupling_strength = np.exp(-0.1 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * (1 + 0.2 * np.sin(x[i] * x[j]))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j) * np.exp(-0.05 * np.abs(x[i] - x[j]))
                
        # Add global scaling with fractal-like frequency components and irregular modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.5 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.sin(0.3 * dist_from_origin))
        
        # Add multi-scale noise component with irregular distribution and fractal characteristics
        noise = 0.02 * np.sum(np.sin(x * 15) * np.cos(x * 7) * np.exp(-0.01 * np.abs(x)))
        result += noise
        
        # Add a complex multi-modal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.5 * np.sin(2 * x[i]) * np.cos(3 * x[i]) + 0.3 * np.sin(4 * x[i])
        result += multimodal
        
        return result