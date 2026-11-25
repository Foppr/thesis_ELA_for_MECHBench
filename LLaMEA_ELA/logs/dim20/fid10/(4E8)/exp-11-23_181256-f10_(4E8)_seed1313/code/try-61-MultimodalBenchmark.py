import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stable computation
        x_scaled = x / 5.0
        
        # Exponential decay terms creating steep gradients
        exp_term = np.sum(np.exp(-np.abs(x_scaled)) * np.cos(2 * np.pi * x_scaled))
        
        # Logarithmic barrier terms preventing boundary crossing
        log_barrier = np.sum(np.log(1 + np.abs(x_scaled)))
        
        # Enhanced polynomial coupling with mixed degrees for varied curvature
        poly_coupling = np.sum(x_scaled**3 * np.sin(x_scaled)) + 0.7 * np.sum(x_scaled**4)
        
        # Chaotic sine modulation with varying frequencies
        chaotic_term = np.sum(np.sin(15 * np.pi * np.sin(x_scaled)))
        
        # New radial barrier term to increase conditioning
        radial_barrier = np.sum((x_scaled**2 + 0.1) * np.log(1 + x_scaled**2))
        
        # Saddle-point interaction terms for complex curvature
        saddle_term = np.sum(x_scaled**2 * np.cos(5 * np.pi * x_scaled))
        
        # Combined function with irregular structure
        return exp_term + log_barrier + poly_coupling + chaotic_term + radial_barrier + 0.15 * np.sum(x_scaled**5) + 0.3 * saddle_term