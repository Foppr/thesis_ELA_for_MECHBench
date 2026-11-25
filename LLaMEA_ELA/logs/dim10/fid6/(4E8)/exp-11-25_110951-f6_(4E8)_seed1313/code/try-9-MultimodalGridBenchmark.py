import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic basin term - global minimum at origin
        basin = np.sum(x_norm**2)
        
        # Multimodal grid terms - create multiple local minima in a grid pattern
        grid_terms = 0.0
        for i in range(self.dim):
            # Create grid of local minima along each dimension with higher frequency
            grid_terms += 15 * np.sin(3 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Additional harmonic terms to increase complexity and create more challenging landscape
        harmonic_terms = 0.0
        for i in range(self.dim):
            harmonic_terms += 7 * np.sin(5 * np.pi * x_norm[i])**2 + 3 * np.cos(5 * np.pi * x_norm[i])
        
        # Coupling terms between dimensions to create interdependencies
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_terms += 2 * np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(np.pi * (x_norm[i] - x_norm[j]))
        
        # Add a small noise-like component to increase fitness variance
        noise_term = 0.5 * np.sum(np.sin(7 * np.pi * x_norm))
        
        return basin + grid_terms + harmonic_terms + coupling_terms + noise_term