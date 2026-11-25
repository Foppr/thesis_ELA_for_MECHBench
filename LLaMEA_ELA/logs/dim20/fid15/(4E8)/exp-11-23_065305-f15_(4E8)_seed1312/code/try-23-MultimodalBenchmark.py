import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Apply a chaotic transformation with exponential decay
        exp_decay = np.exp(-np.sum(x**2) / (2 * self.dim))
        
        # Trigonometric coupling terms
        trig_coupling = np.sum(np.sin(x) * np.cos(2 * x)) / self.dim
        
        # Exponential decay modulated by sinusoidal components
        exponential_mod = np.sum(np.exp(-x**2 / 2) * np.sin(x)) / self.dim
        
        # Polynomial and logarithmic terms for added complexity
        poly_term = np.sum(x**4) / (4 * self.dim)
        log_term = np.sum(np.log(1 + x**2)) / self.dim
        
        # Global minimum at origin with chaotic behavior around it
        result = exp_decay * (trig_coupling + exponential_mod + poly_term + log_term)
        
        # Add a radial component to increase multimodality
        radius = np.sqrt(np.sum(x**2))
        radial_component = 0.3 * np.sin(5 * radius) * np.exp(-radius / 5)
        result += radial_component
        
        return float(result)