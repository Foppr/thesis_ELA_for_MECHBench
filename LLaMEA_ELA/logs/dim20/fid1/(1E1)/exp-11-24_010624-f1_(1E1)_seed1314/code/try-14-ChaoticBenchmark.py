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
        
        # Nested chaotic logistic map component with multi-scale modulation
        for i in range(self.dim):
            # Apply nested logistic maps with varying parameters
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2)
            chaotic_val = self.chaos_params[i] * chaotic_val * (1 - chaotic_val**2)
            # Add multi-scale radial component with harmonic modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with adaptive frequency modulation
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.cos(3 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with fractal-like strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling strength based on distance and angle
                dist = np.sqrt((x[i] - x[j])**2 + (x[i] + x[j])**2)
                angle = np.arctan2(x[j], x[i])
                coupling_strength = np.exp(-0.1 * dist**1.5) * (1 + 0.3 * np.sin(5 * angle))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j)
                
        # Add global scaling with fractal frequency components
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.5 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.sin(0.3 * dist_from_origin))
        
        # Add fractal noise component with multiple interference patterns
        noise = 0.02 * np.sum(np.sin(x * 15) * np.cos(x * 7))
        result += noise
        
        # Add adaptive penalty for regions of high curvature
        curvature_penalty = 0.03 * np.sum(np.abs(x)**3)
        result += curvature_penalty
        
        return result