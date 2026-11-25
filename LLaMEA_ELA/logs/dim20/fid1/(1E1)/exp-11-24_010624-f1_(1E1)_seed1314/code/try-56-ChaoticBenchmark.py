import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with fractal-like variation
        self.chaos_params = np.array([3.5 + 0.3 * np.sin(i * 0.9) + 0.1 * np.cos(i * 0.4) + 0.05 * np.sin(i * 0.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Multi-scale chaotic logistic map component with fractional powers
        for i in range(self.dim):
            # Apply modified logistic map dynamics with fractional exponent
            chaotic_val = self.chaos_params[i] * x[i] * (1 - np.abs(x[i])**1.7)
            # Add radial component with fractional sinusoidal modulation
            radial_term = 0.4 * x[i]**2.3 * np.sin(0.6 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with adaptive frequency modulation
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.cos(1.5 * x[i]) * np.exp(-0.12 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with adaptive strength and perturbed symmetry
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with perturbation
                coupling_strength = np.exp(-0.03 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * (1 + 0.1 * np.sin(x[i] * x[j]))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j) * np.tanh(0.5 * (x[i] + x[j]))
                
        # Add global scaling with multi-frequency components and symmetry breaking
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.tanh(dist_from_origin / 5.0))
        
        # Add noise component with irregular frequency and amplitude
        noise = 0.02 * np.sum(np.sin(x * 15) * np.cos(x * 7))
        result += noise
        
        # Add fractional dimensionality effect
        dim_factor = 1 + 0.05 * np.sum(np.abs(x)**1.3)
        result *= dim_factor
        
        return result