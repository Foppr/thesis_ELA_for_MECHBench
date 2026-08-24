import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for efficiency
        self.c = np.arange(1, dim + 1) * 0.5
        self.sigma = 1.0 / (dim * 2.0)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Gaussian radial basis components with varying centers and widths
        rb_sum = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / self.dim)
            rb_sum += np.exp(-0.5 * ((x_norm - center) / (self.sigma * (i + 1)))**2)
        
        # Trigonometric coupling between dimensions with adaptive frequencies
        coupling = 0.0
        for i in range(self.dim - 1):
            freq = 2.0 + 0.5 * np.sin(i * np.pi / self.dim)
            coupling += np.sin(freq * (x_norm[i] + x_norm[i+1])) * np.cos(freq * (x_norm[i] - x_norm[i+1]))
        
        # Adaptive polynomial barriers that change based on dimension
        barrier = 0.0
        for i in range(self.dim):
            poly_term = (x_norm[i]**2 + 0.5 * x_norm[i]**4 + 0.1 * x_norm[i]**6)
            barrier += poly_term * (1.0 + 0.2 * np.sin(self.c[i] * x_norm[i]))
        
        # Sine-cosine hybrid term for increased complexity
        hybrid = np.sum(np.sin(3.0 * x_norm) * np.cos(2.0 * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Combined fitness with weighted components
        return 0.3 * rb_sum + 0.4 * coupling + 0.2 * barrier + 0.1 * hybrid