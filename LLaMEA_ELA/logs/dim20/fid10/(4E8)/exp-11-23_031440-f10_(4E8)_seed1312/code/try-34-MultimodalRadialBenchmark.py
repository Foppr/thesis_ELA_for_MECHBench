import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Compute radial distance from origin
        r = np.sqrt(np.sum(x_norm**2))
        
        # Base quadratic term with varying conditioning
        quadratic_term = 0.1 * r**2
        
        # Add polynomial interaction terms that create multiple nested basins
        poly_interaction = 0.5 * (r**4 - 2*r**2 + 1)
        
        # Add exponentially decaying sinusoidal perturbations with multiple frequencies
        sine_term = np.sum(np.exp(-5 * r) * (np.sin(10 * np.pi * r)**2 + 
                                            0.5 * np.sin(20 * np.pi * r)**2 + 
                                            0.3 * np.sin(30 * np.pi * r)**2))
        
        # Add cross-dimensional interaction terms with varying weights
        interaction_term = 0.05 * np.sum((x_norm[:-1] * x_norm[1:])**2)
        
        # Add a global minimum at the center with additional penalty for being far from it
        center_penalty = 2 * np.exp(-10 * r**2)
        
        # Combine all terms
        result = quadratic_term + poly_interaction + sine_term + interaction_term + center_penalty
        
        return result