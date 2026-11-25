import numpy as np

class HybridChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize random parameters for each dimension
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, dim)
        self.trig_freq = np.random.uniform(1.0, 5.0, dim)
        self.rbf_centers = np.random.uniform(-3.0, 3.0, dim)
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        self.adaptive_scaling = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial term with mixed degree and adaptive scaling
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += self.poly_coeffs[i] * (x_norm[i] ** (2 + i % 3)) * self.adaptive_scaling[i]
        
        # Trigonometric mixture with varying frequencies
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(self.trig_freq[i] * x_norm[i]) * np.cos(self.trig_freq[i] * x_norm[i] * 0.5)
        
        # Radial Basis Function component with random centers and widths
        rbf_term = 0.0
        for i in range(self.dim):
            rbf_term += np.exp(-np.sum((x_norm - self.rbf_centers[i]) ** 2) / (2 * self.rbf_widths[i] ** 2))
        
        # Cross-dimensional interaction with chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling based on sine and cosine of dimension indices
                coupling_factor = np.sin(i * j * 0.1) * np.cos(i + j * 0.2)
                cross_term += coupling_factor * (x_norm[i] - x_norm[j]) ** 2
        
        # Time-varying stochastic component with dynamic bias
        time_component = np.sum(np.sin(x_norm * 3.0 + np.random.uniform(-0.5, 0.5)) * 
                               np.cos(x_norm * 2.0 + np.random.uniform(-0.3, 0.3)))
        
        # Adaptive dimensionality scaling factor
        dim_scaling = np.sum(self.adaptive_scaling) / self.dim
        
        # Combine all terms with adaptive weights
        combined = (poly_term + trig_term + rbf_term + cross_term + time_component) * dim_scaling
        
        # Add noise and bias to increase complexity
        noise = np.random.normal(0, 0.1) * (1.0 + 0.2 * np.sin(np.sum(x_norm)))
        
        return combined + noise