import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested exponential decay with multiple scales and adaptive exponents
        exp_decay = (np.exp(-np.sum(x**2) / (2 * self.dim)) * 
                    np.exp(-np.sum((x - 1)**2) / (2 * self.dim)) * 
                    np.exp(-np.sum((x + 1)**2) / (2 * self.dim)) * 
                    np.exp(-np.sum((x - 2)**2) / (2 * self.dim)))
        
        # Adaptive frequency sinusoidal coupling with dynamic phase shifts
        freqs = np.arange(1, self.dim + 1)
        trig_coupling = np.sum(np.sin(freqs * x) * np.cos(freqs * x * 1.5)) / self.dim
        
        # Enhanced exponential modulation with polynomial interaction and chaotic scaling
        exponential_mod = np.sum(np.exp(-x**2) * (np.sin(x) + 0.5 * np.cos(2 * x) + 0.3 * np.sin(3 * x) + 
                                                  0.1 * np.sin(7 * x) * np.cos(4 * x))) / self.dim
        
        # Higher-order polynomial and logarithmic terms with chaotic coefficients
        poly_term = (np.sum(x**8) / (8 * self.dim) + 
                    np.sum(x**6) / (6 * self.dim) + 
                    np.sum(x**4) / (4 * self.dim) + 
                    np.sum(x**2) / (2 * self.dim))
        log_term = np.sum(np.log(1 + x**8)) / self.dim
        
        # Enhanced cross-dimensional interaction terms with chaotic coupling
        cross_dim = 0.3 * np.sum(np.sin(x[:-1] - x[1:]) * np.cos(x[:-1] + x[1:]) + 
                                0.2 * np.sin(2 * x[:-1]) * np.cos(3 * x[1:])) / (self.dim - 1)
        
        # Global minimum with chaotic behavior around it using dynamic frequency modulation
        result = exp_decay * (trig_coupling + exponential_mod + poly_term + log_term + cross_dim)
        
        # Add high-frequency radial component for increased multimodality with dynamic scaling
        radius = np.sqrt(np.sum(x**2))
        radial_component = 0.7 * np.sin(20 * radius) * np.exp(-radius / 3) * np.cos(5 * radius)
        result += radial_component
        
        # Add a nested structure with multiple local minima using higher frequency components and chaotic shifts
        nested_term = 0.4 * np.sum(np.sin(11 * x) * np.cos(6 * x) + 
                                 0.3 * np.sin(8 * x) * np.cos(9 * x) + 
                                 0.2 * np.sin(15 * x) * np.cos(3 * x)) / self.dim
        result += nested_term
        
        # Add a chaotic shift to the global minimum with adaptive amplitude and frequency
        shift = 0.15 * np.sum(np.sin(x) * np.cos(2 * x) * np.exp(-x**2) * 
                             np.sin(3 * x) * np.cos(7 * x)) / self.dim
        result += shift
        
        # Add a dynamic chaotic modulation term that changes based on input dimensions
        dynamic_mod = 0.2 * np.sum(np.sin(x * (1 + 0.1 * np.sin(x))) * 
                                 np.cos(x * (1 + 0.1 * np.cos(x)))) / self.dim
        result += dynamic_mod
        
        return float(result)