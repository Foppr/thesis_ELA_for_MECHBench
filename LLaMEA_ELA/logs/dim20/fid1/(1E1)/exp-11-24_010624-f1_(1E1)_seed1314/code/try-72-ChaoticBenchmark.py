import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with enhanced complexity
        self.chaos_params = np.array([3.9 + 0.2 * np.sin(i * 0.8) + 0.1 * np.cos(i * 0.4) + 0.05 * np.sin(i * 1.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with enhanced radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with higher nonlinearity
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**3)
            # Add enhanced radial component with multiple frequency sinusoidal modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with complex frequency modulation and exponential decay
        for i in range(self.dim):
            poly_term = 0.1 * x[i]**6 * np.cos(3 * x[i]) * np.exp(-0.2 * np.abs(x[i])) * np.sin(0.5 * x[i])
            result += poly_term
            
        # Add cross-dimensional coupling with variable strength and phase shift
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with complex interaction
                coupling_strength = np.exp(-0.1 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * np.sin(0.5 * (x[i]**2 + x[j]**2))
                phase_shift = np.cos(i * 0.3) * np.sin(j * 0.4)
                result += coupling_strength * np.sin(x[i] * x[j]) * phase_shift
                
        # Add global scaling with multiple frequency components and dynamic modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.exp(-0.05 * dist_from_origin))
        
        # Add enhanced noise component with multiple frequency sources
        noise = 0.02 * np.sum(np.sin(x * 15) + 0.5 * np.cos(x * 8))
        result += noise
        
        # Add a small but significant perturbation to create more complex basins
        perturbation = 0.005 * np.sum(np.sin(x * 20) * np.cos(x * 10))
        result += perturbation
        
        return result