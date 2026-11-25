import numpy as np

class MultiModalAdaptiveLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and widths for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-1, 1, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with multiple peaks
        rbf_sum = 0.0
        for i in range(10):
            diff = x_norm - self.centers[i]
            rbf_sum += np.exp(-np.sum(diff**2) / (2 * self.widths[i]**2))
        
        # Adaptive noise injection based on position
        noise_amp = 0.5 * (1 + np.sin(np.sum(x_norm**2)))
        noise = np.random.normal(0, noise_amp, self.dim)
        
        # Directional gradient modulation with adaptive scaling
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += (x_norm[i]**3) * np.cos(x_norm[i]) * np.sin(i * np.pi / self.dim)
        
        # Cross-dimensional coupling with sine-wave interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x_norm[i] * x_norm[j]) * (i + j) / (self.dim**2)
        
        # Polynomial shaping with mixed exponents
        poly_shape = 0.0
        for i in range(self.dim):
            if i % 3 == 0:
                poly_shape += x_norm[i]**4
            elif i % 3 == 1:
                poly_shape += x_norm[i]**5
            else:
                poly_shape += x_norm[i]**6
        
        # Combine components with dynamic weights that depend on position
        pos_dependent_weight = 0.5 + 0.5 * np.tanh(np.sum(x_norm**2) - 1.0)
        
        result = (rbf_sum + grad_mod + cross_coupling + poly_shape) * pos_dependent_weight
        
        # Add conditioning through higher-order terms
        conditioning = 0.1 * np.sum(np.abs(x_norm)**3)
        
        return result + conditioning