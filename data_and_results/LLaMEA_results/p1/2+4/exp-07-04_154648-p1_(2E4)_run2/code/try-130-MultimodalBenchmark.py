import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        self.sin_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.cos_frequencies = np.random.uniform(1.0, 8.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Trigonometric components with varying frequencies
        trig_sum = 0.0
        for i in range(self.dim):
            trig_sum += np.sin(self.sin_frequencies[i] * x_norm[i]) * \
                       np.cos(self.cos_frequencies[i] * x_norm[i]) * \
                       (1.0 + 0.3 * np.sin(2.0 * x_norm[i]))
        
        # Radial basis functions with adaptive centers
        rbf_sum = 0.0
        for i in range(10):
            diff = x_norm - self.rbf_centers[i]
            # Widths adapt based on the distance from the origin
            adaptive_width = self.rbf_widths[i] * (1.0 + 0.2 * np.linalg.norm(x_norm))
            rbf_sum += np.exp(-0.5 * np.sum((diff / adaptive_width)**2))
        
        # Cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_norm[i] * x_norm[j]) * \
                             np.sin(np.pi * (x_norm[i] + x_norm[j])) * \
                             np.cos(np.pi * (x_norm[i] - x_norm[j]))
        
        # Polynomial and interaction components
        poly_term = 0.05 * np.sum(x_norm**6)
        interaction_term = 0.03 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Combine all components
        return trig_sum + rbf_sum + cross_term + poly_term + interaction_term