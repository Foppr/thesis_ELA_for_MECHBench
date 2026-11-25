import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested exponential decay with multiple scales
        exp_decay = (np.exp(-np.sum(x**2) / (2 * self.dim)) * 
                    np.exp(-np.sum((x - 1)**2) / (2 * self.dim)) * 
                    np.exp(-np.sum((x + 1)**2) / (2 * self.dim)))
        
        # Multiple trigonometric coupling terms with different frequencies and phases
        trig_coupling = (np.sum(np.sin(x) * np.cos(3 * x)) + 
                        np.sum(np.sin(2 * x) * np.cos(x)) + 
                        np.sum(np.sin(0.5 * x) * np.cos(4 * x)) + 
                        np.sum(np.sin(1.5 * x) * np.cos(2.5 * x))) / self.dim
        
        # Enhanced exponential modulation with polynomial interaction
        exponential_mod = np.sum(np.exp(-x**2) * (np.sin(x) + 0.5 * np.cos(2 * x) + 0.3 * np.sin(3 * x))) / self.dim
        
        # Higher-order polynomial and logarithmic terms for complexity
        poly_term = (np.sum(x**6) / (6 * self.dim) + 
                    np.sum(x**4) / (4 * self.dim) + 
                    np.sum(x**2) / (2 * self.dim))
        log_term = np.sum(np.log(1 + x**6)) / self.dim
        
        # Enhanced cross-dimensional interaction terms
        cross_dim = 0.5 * np.sum(np.sin(x[:-1] - x[1:]) + 0.3 * np.cos(x[:-1] + x[1:])) / (self.dim - 1)
        
        # Global minimum with chaotic behavior around it
        result = exp_decay * (trig_coupling + exponential_mod + poly_term + log_term + cross_dim)
        
        # Add high-frequency radial component for increased multimodality
        radius = np.sqrt(np.sum(x**2))
        radial_component = 0.5 * np.sin(15 * radius) * np.exp(-radius / 4)
        result += radial_component
        
        # Add a nested structure with multiple local minima using higher frequency components
        nested_term = 0.3 * np.sum(np.sin(9 * x) * np.cos(4 * x) + 0.5 * np.sin(5 * x) * np.cos(7 * x)) / self.dim
        result += nested_term
        
        # Add a chaotic shift to the global minimum to make optimization harder
        shift = 0.1 * np.sum(np.sin(x) * np.cos(2 * x) * np.exp(-x**2)) / self.dim
        result += shift
        
        return float(result)