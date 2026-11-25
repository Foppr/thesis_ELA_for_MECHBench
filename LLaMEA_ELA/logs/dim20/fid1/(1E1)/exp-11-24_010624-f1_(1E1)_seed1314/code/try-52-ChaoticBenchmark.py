import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with fractal-like complexity
        self.chaos_params = np.array([3.5 + 0.8 * np.sin(i * 1.2 + 1.0) * np.cos(i * 0.7) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal-like chaotic component with complex dynamics
        for i in range(self.dim):
            # Apply a modified logistic map with complex coupling
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2) + 0.1 * np.sin(x[i] * 3)
            # Add radial and angular components
            radial_term = 0.2 * x[i]**3 * np.cos(0.4 * x[i])
            angular_term = 0.15 * x[i] * np.sin(0.6 * x[i]**2)
            result += chaotic_val + radial_term + angular_term
            
        # Add higher-order polynomial terms with complex frequency modulation
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.cos(3 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            result += poly_term
            
        # Add enhanced cross-dimensional coupling with fractal-like interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling strength based on distance and angle
                dist = np.sqrt((x[i] - x[j])**2 + (x[i] + x[j])**2)
                angle = np.arctan2(x[j], x[i])
                coupling_strength = np.exp(-0.1 * dist) * (1 + 0.3 * np.sin(5 * angle))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j) * np.tanh(dist)
                
        # Add global scaling with fractal frequency components
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.5 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.tanh(dist_from_origin))
        
        # Add a novel noise component with fractal characteristics
        noise = 0.02 * np.sum(np.sin(x * 15) * np.cos(x * 7))
        result += noise
        
        # Add a final complex modulation based on all dimensions
        final_mod = np.prod(np.sin(x * 0.5 + 1.0)) * np.sum(np.cos(x * 0.3))
        result += 0.05 * final_mod
        
        return result