import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic exponential decay component
        exp_decay = np.exp(-np.sum(x**2) / (2 * self.dim))
        
        # Enhanced trigonometric coupling with modified frequencies
        trig_coupling = np.sum(np.sin(4 * x) * np.cos(6 * x) + np.sin(8 * x) * np.cos(12 * x)) / self.dim
        
        # Multi-scale exponential modulation
        exponential_mod = np.sum(np.exp(-x**2 / 2) * (np.sin(x) + 0.5 * np.sin(3 * x))) / self.dim
        
        # Added quartic polynomial term for increased curvature
        poly_term = np.sum(x**4) / (4 * self.dim)
        log_term = np.sum(np.log(1 + x**4)) / self.dim
        
        # Cross-dimensional interference terms
        cross_dim = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim += np.sin(x[i] * x[j]) / (1 + abs(x[i] - x[j]))
        cross_dim /= (self.dim * (self.dim - 1) / 2)
        
        # Global minimum shifted to a non-zero point with chaotic behavior
        shift = np.ones(self.dim) * 0.5
        result = exp_decay * (trig_coupling + exponential_mod + poly_term + log_term + cross_dim)
        
        # Enhanced radial component with more pronounced peaks
        radius = np.sqrt(np.sum(x**2))
        radial_component = 0.7 * np.sin(12 * radius) * np.cos(4 * radius) * np.exp(-radius / 4)
        
        # Add chaotic noise term to increase multimodality
        noise = 0.15 * np.sum(np.sin(14 * x) * np.cos(8 * x)) / self.dim
        
        result += radial_component + noise
        
        return float(result)