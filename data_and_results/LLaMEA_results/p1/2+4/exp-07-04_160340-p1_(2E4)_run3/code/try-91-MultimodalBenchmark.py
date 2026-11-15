import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-1, 1] for internal computations
        x_norm = x / 5.0
        
        # Base quadratic term
        base = np.sum(x_norm**2)
        
        # Fractal-like sinusoidal components with varying frequencies and amplitudes
        fractal_term = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)  # Varying frequencies
            amp = 1.0 / (1.0 + i * 0.1)  # Decreasing amplitudes
            fractal_term += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Dynamic scaling based on position
        scale_factor = 1.0
        for i in range(self.dim):
            scale_factor *= (1.0 + 0.5 * np.sin(10 * x_norm[i]))
        
        # Multiple nested global minima with varying depths and positions
        minima_positions = [
            np.array([0.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim),
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.25] * self.dim),
            np.array([-0.25] * self.dim),
            np.array([0.75] * self.dim),
            np.array([-0.75] * self.dim)
        ]
        
        # Penalty for proximity to global minima
        penalty = 0.0
        for i, pos in enumerate(minima_positions):
            dist = np.sum((x_norm - pos)**2)
            penalty += np.exp(-dist / (2.0 * 0.1**2)) * (1.0 + 0.5 * np.sin(i * np.pi / 4.0))
        
        # Chaotic modulation using a logistic map
        chaotic_mod = 1.0
        for i in range(self.dim):
            chaotic_mod *= (4.0 * x_norm[i] * (1.0 - x_norm[i]))
        
        # Add a dynamic component that changes based on the current evaluation
        dynamic_component = 0.0
        for i in range(self.dim):
            dynamic_component += np.sin(20 * x_norm[i]) * np.cos(15 * x_norm[i]) * np.exp(-0.5 * i)
        
        # Combine all components
        result = base + 0.5 * fractal_term + penalty + chaotic_mod + dynamic_component
        
        # Add a self-similar structure with multiple scales
        self_similar = 0.0
        for scale in [2, 4, 8]:
            for i in range(self.dim):
                self_similar += np.sin(scale * x_norm[i]) * np.cos(scale * x_norm[i])
        
        result += 0.1 * self_similar
        
        return result