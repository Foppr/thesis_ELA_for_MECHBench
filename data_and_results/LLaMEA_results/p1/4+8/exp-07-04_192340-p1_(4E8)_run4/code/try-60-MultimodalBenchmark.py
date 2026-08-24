import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for self-similarity
        self.fractal_params = np.random.rand(dim) * 2 + 1
        # Hierarchical conditioning factors
        self.conditioning_factors = np.array([1.0 + 0.1 * np.sin(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply hierarchical conditioning
        x_cond = x * self.conditioning_factors
        
        # Compute fractal-like multimodal function
        result = 0.0
        for i in range(self.dim):
            # Base quadratic term
            result += (x_cond[i] ** 2) * (i + 1)
            # Fractal periodic components with varying frequencies
            freq = self.fractal_params[i] * (i + 1)
            result += 3 * np.sin(x_cond[i] * freq * np.pi / 2) * np.cos(x_cond[i] * freq * np.pi / 4)
            # Self-similar ridge structures
            result += 2 * np.sin(x_cond[i] * freq * np.pi) * np.cos(x_cond[i] * freq * np.pi / 2)
            # Multi-scale chaotic modulation
            result += 1.5 * np.sin(x_cond[i] * freq * np.pi * 3) * np.cos(x_cond[i] * freq * np.pi * 2)
            # Hierarchical saddle points
            result += 0.8 * np.sin(2 * x_cond[i]) * np.cos(2 * x_cond[i]) * (1 + 0.2 * np.sin(i * 0.5))
            # Fractal basin depth modulation
            result += 0.5 * np.sin(x_cond[i] * freq * np.pi * 0.5) ** 3
        
        # Add fractal scaling term for hierarchical complexity
        fractal_scale = np.prod(np.abs(x_cond) + 1.0)
        result *= (1.0 + 0.3 * fractal_scale)
        
        # Add global minimum with fractal penalty
        result += 0.02 * np.sum(np.abs(x) ** 3)
        
        # Add hierarchical conditioning effect
        result *= np.prod(self.conditioning_factors)
        
        return result