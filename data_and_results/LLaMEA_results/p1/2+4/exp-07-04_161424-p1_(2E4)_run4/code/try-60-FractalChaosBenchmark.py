import numpy as np

class FractalChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors for multi-scale structure
        self.fractal_factors = np.array([0.5 ** i for i in range(dim)])
        # Precompute trigonometric chaos parameters
        self.chaos_params = np.random.uniform(0.1, 2.0, dim)
        # Precompute gradient conditioning weights
        self.conditioning_weights = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Multi-scale fractal pattern using sine and cosine combinations
        fractal_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            scale = self.fractal_factors[i]
            # Combine multiple frequencies for fractal structure
            fractal_pattern[i] = (np.sin(x_norm[i] * self.chaos_params[i]) * 
                                np.cos(x_norm[i] * self.chaos_params[i] * 2) * 
                                np.sin(x_norm[i] * self.chaos_params[i] * 3) * 
                                scale)
        
        # Gradient-dependent conditioning with exponential scaling
        conditioning = np.sum(self.conditioning_weights * np.exp(np.abs(x_norm)))
        
        # Trigonometric chaos with phase shifts
        chaos_component = np.sum(np.sin(x_norm * self.chaos_params + np.pi/4) * 
                               np.cos(x_norm * self.chaos_params * 1.5 + np.pi/3))
        
        # Multi-modal interaction using polynomial and fractal components
        interaction = np.sum(fractal_pattern**2 + 0.3 * fractal_pattern**3 + 0.01 * fractal_pattern**4)
        
        # Add self-similarity through recursive scaling
        self_similarity = np.sum(np.abs(x_norm) * np.sin(x_norm * np.pi * 2))
        
        # Combine all components with dynamic weighting
        total = 0.3 * interaction + 0.25 * chaos_component + 0.2 * conditioning + 0.15 * self_similarity
        
        # Add dimensionality-dependent complexity factor
        complexity_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return total * complexity_factor