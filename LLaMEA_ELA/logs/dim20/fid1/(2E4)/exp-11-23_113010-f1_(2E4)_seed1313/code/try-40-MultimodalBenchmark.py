import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Gaussian radial basis functions with varying widths and heights
        rb_sum = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                dist = np.sum((x_norm - centers[i])**2)
                rb_sum += 2.0 * np.exp(-5.0 * dist) * (1.0 + 0.5 * np.sin(10 * dist))
        
        # Trigonometric plateau structure with adaptive frequencies
        plateau = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i)
            plateau += np.cos(freq * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Adaptive conditioning with dimension-dependent scaling
        cond_factor = 1.0
        for i in range(self.dim):
            cond_factor *= (1.0 + 0.1 * (i + 1) * np.abs(x_norm[i]))
        
        # Cross-dimensional interaction through exponential coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-2.0 * (x_norm[i] - x_norm[j])**2) * np.sin(3 * (x_norm[i] + x_norm[j]))
        
        # Saddle point enhancement with hyperbolic tangent modulation
        saddle = 0.0
        for i in range(self.dim):
            saddle += np.tanh(2.0 * x_norm[i]) * np.cos(4 * x_norm[i])
        
        # Add noise and scale the final result
        noise = 0.01 * np.random.random()
        
        return 1.5 * rb_sum + 0.8 * plateau + 0.6 * cond_factor + 0.7 * cross_term + 0.5 * saddle + noise