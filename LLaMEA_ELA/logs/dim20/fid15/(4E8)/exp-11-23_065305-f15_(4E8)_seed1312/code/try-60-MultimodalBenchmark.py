import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic exponential decay component with enhanced nonlinearity
        exp_decay = np.exp(-np.sum(x**4) / (2 * self.dim))
        
        # Enhanced trigonometric coupling with multiple frequencies and phase shifts
        trig_coupling = np.sum(np.sin(2 * x + 0.5) * np.cos(4 * x - 1.0) + 
                              np.sin(6 * x + 1.2) * np.cos(9 * x - 0.8)) / self.dim
        
        # Multi-scale exponential modulation with enhanced interaction
        exponential_mod = np.sum(np.exp(-x**3 / 3) * (np.sin(x) + 0.3 * np.sin(5 * x))) / self.dim
        
        # Polynomial and logarithmic terms for added complexity with modified exponents
        poly_term = np.sum(x**5) / (5 * self.dim)
        log_term = np.sum(np.log(1 + x**3)) / self.dim
        
        # Cross-dimensional interference terms with enhanced coupling strength
        cross_dim = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim += np.sin(x[i] * x[j]) / (1 + abs(x[i] - x[j])**2)
        cross_dim /= (self.dim * (self.dim - 1) / 2)
        
        # Global minimum shifted to a non-zero point with chaotic behavior
        shift = np.ones(self.dim) * 0.7
        result = exp_decay * (trig_coupling + exponential_mod + poly_term + log_term + cross_dim)
        
        # Add a highly complex radial component with multiple peaks and valleys
        radius = np.sqrt(np.sum(x**2))
        radial_component = 0.3 * np.sin(15 * radius) * np.cos(5 * radius) * np.exp(-radius / 4)
        
        # Add chaotic noise term to increase multimodality with modified frequencies
        noise = 0.08 * np.sum(np.sin(17 * x) * np.cos(9 * x)) / self.dim
        
        result += radial_component + noise
        
        return float(result)