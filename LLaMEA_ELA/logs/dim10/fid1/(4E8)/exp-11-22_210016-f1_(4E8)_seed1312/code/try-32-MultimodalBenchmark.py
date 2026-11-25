import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher degrees and non-uniform scaling
        poly_term = 0.5 * np.sum(x**2) + 0.1 * np.sum(x**5) + 0.05 * np.sum(x**6)
        
        # Complex sinusoidal oscillations with multiple frequencies and phase shifts
        sin_term = np.sum(np.sin(12.0 * x) + 0.5 * np.sin(24.0 * x) + 0.3 * np.sin(36.0 * x))
        
        # Advanced cross-term interactions including ternary and weighted combinations
        cross_term = 0.3 * np.sum(x[:-1] * x[1:])
        quad_cross = 0.2 * np.sum((x[:-1] + x[1:]) ** 2)
        cubic_cross = 0.1 * np.sum(x[:-2] * x[1:-1] * x[2:])
        
        # Novel non-uniform scaling and additional interaction terms
        scale_factor = np.arange(1, self.dim + 1) / self.dim
        scaled_term = np.sum(scale_factor * x**3)
        
        # Additional chaotic-like modulation using cosine and exponential components
        modulate_term = np.sum(np.cos(5.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combine all terms
        result = poly_term + sin_term + cross_term + quad_cross + cubic_cross + scaled_term + modulate_term
        
        return result