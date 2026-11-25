import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic exponential decay component with enhanced curvature
        exp_decay = np.exp(-np.sum(x**2) / (2 * self.dim)) * (1 + 0.1 * np.sin(5 * np.sum(x**2)))
        
        # Enhanced trigonometric coupling with modified frequencies and phase shifts
        trig_coupling = np.sum(np.sin(3 * x + 0.5) * np.cos(7 * x + 1.0) + 
                              np.sin(9 * x + 1.5) * np.cos(13 * x + 2.0)) / self.dim
        
        # Multi-scale exponential modulation with additional chaotic components
        exponential_mod = np.sum(np.exp(-x**2 / 2) * (np.sin(x) + 0.3 * np.sin(3 * x) + 
                                                       0.2 * np.sin(5 * x))) / self.dim
        
        # Added quartic polynomial term for increased curvature and additional chaos
        poly_term = np.sum(x**4) / (4 * self.dim)
        log_term = np.sum(np.log(1 + x**4)) / self.dim
        
        # Cross-dimensional interference terms with enhanced coupling strength
        cross_dim = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim += np.sin(x[i] * x[j]) / (1 + abs(x[i] - x[j])) * np.exp(-abs(x[i] - x[j]) / 2)
        cross_dim /= (self.dim * (self.dim - 1) / 2)
        
        # Global minimum shifted to a non-zero point with chaotic behavior
        shift = np.ones(self.dim) * 0.7
        result = exp_decay * (trig_coupling + exponential_mod + poly_term + log_term + cross_dim)
        
        # Enhanced radial component with more pronounced peaks and additional chaos
        radius = np.sqrt(np.sum(x**2))
        radial_component = 0.8 * np.sin(15 * radius) * np.cos(5 * radius) * np.exp(-radius / 3) + \
                          0.3 * np.sin(25 * radius) * np.cos(10 * radius) * np.exp(-radius / 5)
        
        # Add chaotic noise term to increase multimodality and complexity
        noise = 0.2 * np.sum(np.sin(16 * x) * np.cos(9 * x) + 
                            0.5 * np.sin(20 * x) * np.cos(11 * x)) / self.dim
        
        # Add a new chaotic radial basis function component
        rbf_component = 0.15 * np.sum(np.exp(-np.abs(x) / 2) * np.sin(7 * x)) / self.dim
        
        result += radial_component + noise + rbf_component
        
        return float(result)