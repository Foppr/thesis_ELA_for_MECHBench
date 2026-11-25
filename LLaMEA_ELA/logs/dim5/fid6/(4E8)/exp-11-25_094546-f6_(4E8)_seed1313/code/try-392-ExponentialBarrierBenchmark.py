import numpy as np

class ExponentialBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Base polynomial term with varying degree
            base = 0.5 * xi**4 + 0.3 * xi**3 + 0.1 * xi**2
            
            # Exponential decay interactions with neighbors
            exp_interaction = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    decay_factor = np.exp(-2.0 * distance)
                    exp_interaction += decay_factor * np.sin(5 * xi + 3 * x_norm[j])
            
            # Polynomial coupling with higher-order terms
            poly_coupling = 0.0
            for k in range(1, 6):
                poly_coupling += (0.2 / k) * (xi**k) * np.cos(k * x_norm[(i+k) % self.dim])
            
            # Logarithmic barrier function with adaptive threshold
            barrier = 0.0
            for j in range(self.dim):
                diff = abs(xi - x_norm[j])
                if diff < 0.1:
                    barrier += 10.0 * np.log(1.0 + 100.0 * diff**2)
            
            # Sharp gradient component with sinusoidal modulation
            sharp_gradient = 2.0 * np.sin(10 * xi) * np.cos(7 * xi) + 0.5 * np.sin(15 * xi)
            
            # Dimensional scaling with exponential growth factor
            dim_scaling = 1.0 + 0.5 * np.exp(0.1 * i) * np.sin(0.3 * self.dim)
            
            # Add all components together
            result += (base + exp_interaction + poly_coupling + barrier + sharp_gradient) * dim_scaling
            
        # Global normalization and dimension-dependent correction
        global_norm = 1.0 + 0.1 * np.sin(self.dim * 0.5) + 0.05 * np.cos(self.dim * 0.2)
        
        return global_norm * result / self.dim