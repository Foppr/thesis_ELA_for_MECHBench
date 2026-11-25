import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with more complex variation
        self.chaos_params = np.array([3.8 + 0.1 * np.sin(i * 0.7) + 0.05 * np.cos(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with enhanced nonlinearity and radial symmetry
        for i in range(self.dim):
            # Apply modified logistic map dynamics with cubic term for increased chaos
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**3)
            # Add radial component with enhanced sinusoidal modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.6 * x[i]) * np.cos(0.2 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation and exponential decay
        for i in range(self.dim):
            poly_term = 0.07 * x[i]**6 * np.cos(1.5 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with adaptive strength and phase shift
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with quadratic interaction
                coupling_strength = np.exp(-0.03 * ((x[i] - x[j])**2 + (x[i] + x[j])**2))
                # Add phase shift to increase complexity
                phase_shift = np.sin(0.5 * (i - j)) * np.cos(0.3 * (i + j))
                result += coupling_strength * np.sin(x[i] * x[j]) * phase_shift
                
        # Add global scaling with multiple frequency components and adaptive factor
        dist_from_origin = np.sqrt(np.sum(x**2))
        # Use more complex modulation for global scaling
        global_factor = 1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.6 * dist_from_origin)
        result *= global_factor
        
        # Add noise component with increased variability to boost irregularity
        noise = 0.015 * np.sum(np.sin(x * 12))
        result += noise
        
        return result