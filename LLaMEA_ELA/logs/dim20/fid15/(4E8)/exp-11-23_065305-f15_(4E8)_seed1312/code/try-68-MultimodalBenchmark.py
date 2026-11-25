import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Highly chaotic radial basis functions with adaptive scaling
        rbf = np.sum(np.exp(-np.sum((x - np.linspace(-1, 1, self.dim))**2) / (2 * (0.5 + 0.5 * np.sin(self.dim)))) * 
                     np.sin(np.sum(x**2) * (1 + 0.1 * np.sin(self.dim))) * 
                     np.cos(np.sum(x) * (1 + 0.2 * np.cos(self.dim))))
        
        # Dynamic phase-shifted sinusoidal coupling with frequency modulation
        freq_mod = np.sum(np.sin(x * (1 + 0.3 * np.sin(self.dim)) + 0.5 * np.cos(x)) * 
                         np.cos(2 * x * (1 + 0.2 * np.cos(self.dim)) + 0.3 * np.sin(x))) / self.dim
        
        # Multi-scale exponential decay with chaotic amplitude variation
        multi_scale_decay = np.sum(np.exp(-np.sum((x - np.random.rand(self.dim))**2) / (2 * (1 + 0.2 * np.sin(self.dim)))) * 
                                  np.exp(-np.sum((x + np.random.rand(self.dim))**2) / (2 * (1 + 0.3 * np.cos(self.dim)))))
        
        # Nested chaotic structure with higher-order polynomial and logarithmic interactions
        nested_structure = np.sum(np.sin(5 * x) * np.cos(3 * x) * np.exp(-x**2) + 
                                 np.cos(7 * x) * np.sin(4 * x) * np.log(1 + x**4)) / self.dim
        
        # Cross-dimensional interference with dynamic coupling strength
        cross_dim = 0.7 * np.sum(np.sin(x[:-1] * (1 + 0.1 * np.sin(self.dim)) - x[1:] * (1 + 0.1 * np.cos(self.dim))) + 
                               0.4 * np.cos(x[:-1] * (1 + 0.2 * np.cos(self.dim)) + x[1:] * (1 + 0.2 * np.sin(self.dim)))) / (self.dim - 1)
        
        # High-frequency chaotic radial component with variable amplitude
        radius = np.sqrt(np.sum(x**2))
        chaotic_radial = 0.8 * np.sin(20 * radius + 0.5 * np.sin(3 * radius)) * np.exp(-radius / 5)
        
        # Adaptive dimensional coupling with chaotic phase shifts
        dim_coupling = np.sum(np.sin(x * (1 + 0.4 * np.sin(self.dim))) * 
                             np.cos(x * (1 + 0.3 * np.cos(self.dim))) * 
                             np.exp(-x**2)) / self.dim
        
        # Combined result with chaotic scaling factor
        result = rbf * freq_mod * multi_scale_decay * (nested_structure + cross_dim + chaotic_radial + dim_coupling)
        
        # Add a highly complex chaotic shift to global minimum for increased difficulty
        chaotic_shift = 0.2 * np.sum(np.sin(x * (1 + 0.5 * np.sin(self.dim))) * 
                                   np.cos(x * (1 + 0.4 * np.cos(self.dim))) * 
                                   np.exp(-x**3)) / self.dim
        
        result += chaotic_shift
        
        return float(result)