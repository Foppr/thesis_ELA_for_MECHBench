import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for stability
        self.fractal_dims = np.linspace(0.5, 2.0, min(dim, 10))
        self.scaling_factors = np.logspace(-1, 1, min(dim, 10))
        
    def f(self, x):
        # Clamp input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Fractal multimodal components with self-similarity
        for i in range(min(self.dim, 10)):
            # Dynamic scaling based on dimension
            scale = self.scaling_factors[i % len(self.scaling_factors)]
            fractal_dim = self.fractal_dims[i % len(self.fractal_dims)]
            
            # Fractal-like multimodal function using sine and cosine
            term = scale * (np.sin(x[i] * np.pi * 2**fractal_dim) + 
                           np.cos(x[i] * np.pi * 2**(fractal_dim + 0.5)))
            
            # Add dimension-dependent modulation
            result += term * (1.0 + 0.3 * np.sin(i * 0.7))
        
        # Gradient-dependent noise component
        grad_noise = 0.0
        for i in range(self.dim):
            if i > 0:
                grad_diff = abs(x[i] - x[i-1])
                grad_noise += 0.2 * np.exp(-grad_diff**2) * np.sin(x[i] * 5)
        
        # Add dynamic scaling based on input magnitude
        magnitude_factor = 1.0 + 0.1 * np.sum(np.abs(x)) / self.dim
        
        return result * magnitude_factor + grad_noise