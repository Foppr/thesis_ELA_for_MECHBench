import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.time_factor = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal components with fractional frequencies and dynamic modulation
        sin_term = 0.0
        for i in range(8):
            freq = 2**(i+1) * (1 + 0.3 * np.sin(0.1 * i * x_norm.sum()))
            sin_term += np.sum(np.sin(freq * x_norm) * np.cos(freq * x_norm**1.7))
        
        # Enhanced multi-modal radial basis functions with dynamic widths
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            width = self.rbf_widths[i] * (1 + 0.2 * np.sin(0.05 * i * x_norm.sum()))
            rbf_sum += np.exp(-0.5 * np.sum((diff / width)**2)) * np.cos(3 * np.pi * i * x_norm.sum())
        
        # Time-dependent noise with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i] * self.time_factor[i]) * np.cos(x_norm[i]**2.3) * np.sin(0.1 * x_norm.sum())
        
        # Cross-dimensional coupling with chaotic interaction terms
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            j = (i + 1) % self.dim
            interaction = np.sin(3 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
            cross_interaction += interaction * (1 + 0.1 * np.sin(0.5 * x_norm.sum()))
        
        # Fractional polynomial and chaotic global term
        poly_term = 0.01 * np.sum(np.abs(x_norm)**3.7)
        chaotic_global = 0.05 * np.sin(10 * x_norm.sum()) * np.cos(5 * x_norm.sum()**2)
        
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + chaotic_global