import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Nested exponential decay with varying rates
        exp_decay = np.exp(-np.sum(x**2) / (2 * self.dim)) * np.exp(-np.sum((x - 1)**2) / (2 * self.dim))
        
        # Multiple trigonometric coupling terms with different frequencies
        trig_coupling = (np.sum(np.sin(x) * np.cos(3 * x)) + 
                        np.sum(np.sin(2 * x) * np.cos(x)) + 
                        np.sum(np.sin(0.5 * x) * np.cos(4 * x))) / self.dim
        
        # Exponential modulation with polynomial interaction
        exponential_mod = np.sum(np.exp(-x**2) * (np.sin(x) + 0.5 * np.cos(2 * x))) / self.dim
        
        # Higher-order polynomial and logarithmic terms for complexity
        poly_term = (np.sum(x**6) / (6 * self.dim) + 
                    np.sum(x**3) / (3 * self.dim))
        log_term = np.sum(np.log(1 + x**4)) / self.dim
        
        # Cross-dimensional interaction terms
        cross_dim = 0.5 * np.sum(np.sin(x[:-1] - x[1:])) / (self.dim - 1)
        
        # Global minimum with chaotic behavior around it
        result = exp_decay * (trig_coupling + exponential_mod + poly_term + log_term + cross_dim)
        
        # Add high-frequency radial component for increased multimodality
        radius = np.sqrt(np.sum(x**2))
        radial_component = 0.5 * np.sin(10 * radius) * np.exp(-radius / 3)
        result += radial_component
        
        # Add a nested structure with multiple local minima
        nested_term = 0.2 * np.sum(np.sin(7 * x) * np.cos(3 * x)) / self.dim
        result += nested_term
        
        return float(result)