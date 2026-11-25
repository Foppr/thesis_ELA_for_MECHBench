import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with nested logistic map structure
        self.chaos_params = np.array([3.9 + 0.2 * np.sin(i * 0.8) + 0.1 * np.cos(i * 0.4) + 0.05 * np.sin(i * 0.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Nested chaotic logistic map component with multiple feedback loops
        for i in range(self.dim):
            # Apply nested logistic dynamics
            val1 = self.chaos_params[i] * x[i] * (1 - x[i]**2)
            val2 = 3.8 * val1 * (1 - val1**2)
            chaotic_val = val1 + 0.5 * val2
            # Add radial component with multiple harmonic frequencies
            radial_term = 0.4 * x[i]**2 * np.sin(0.6 * x[i]) + 0.2 * x[i]**3 * np.cos(0.4 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with dynamic frequency modulation
        for i in range(self.dim):
            poly_term = 0.1 * x[i]**6 * np.sin(3 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with time-delayed interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-delayed coupling with dynamic strength
                delay_strength = np.exp(-0.03 * ((x[i] - x[j])**2 + (x[i] + x[j])**2))
                delayed_interaction = np.sin(x[i] * x[j]) * np.cos(i - j) * np.sin(0.5 * (x[i] + x[j]))
                result += delay_strength * delayed_interaction
                
        # Add global scaling with fractal-like frequency components
        dist_from_origin = np.sqrt(np.sum(x**2))
        fractal_factor = 1 + 0.2 * np.sin(0.5 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.sin(0.3 * dist_from_origin)
        result *= fractal_factor
        
        # Add multi-scale noise component for increased irregularity
        noise = 0.02 * np.sum(np.sin(x * 15) + 0.5 * np.cos(x * 7))
        result += noise
        
        # Add self-coupling with non-linear transformation
        self_coupling = 0.03 * np.sum(np.sin(x**3) * np.cos(x**2))
        result += self_coupling
        
        return result