import numpy as np

class SinusoidalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Precompute sinusoidal frequencies and amplitudes
        self.frequencies = np.random.uniform(1.0, 10.0, dim) * 2.0
        self.amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_weights = np.random.uniform(-2.0, 2.0, 10)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base sinusoidal component with varying frequencies and amplitudes
        f_val = 0.0
        for i in range(self.dim):
            f_val += self.amplitudes[i] * np.sin(self.frequencies[i] * np.pi * x_norm[i])
            
        # Add gradient-based conditioning
        grad_conditioning = 0.0
        for i in range(self.dim):
            if i > 0:
                grad_conditioning += (x_norm[i] - x_norm[i-1])**2
        f_val += 0.5 * grad_conditioning
        
        # Radial basis function interactions
        rbf_sum = 0.0
        for i in range(10):
            rbf_term = 0.0
            for j in range(self.dim):
                rbf_term += (x_norm[j] - self.rbf_centers[i, j])**2
            rbf_sum += self.rbf_weights[i] * np.exp(-0.5 * rbf_term)
            
        f_val += 0.3 * rbf_sum
        
        # Multi-scale harmonic interference
        interference = 0.0
        for scale in [0.5, 1.0, 2.0]:
            for i in range(self.dim):
                interference += np.sin(scale * 4 * np.pi * x_norm[i]) * np.cos(scale * 3 * np.pi * x_norm[i])
        f_val += 0.2 * interference
        
        # Cross-term coupling with non-separable interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_norm[i] * x_norm[j]) * np.sin(2 * np.pi * (x_norm[i] + x_norm[j]))
        f_val += 0.15 * cross_term
        
        # Adaptive conditioning based on position
        adaptive_condition = 0.0
        for i in range(self.dim):
            adaptive_condition += (np.abs(x_norm[i]) ** (1.5 + 0.5 * np.sin(3 * np.pi * x_norm[i])))
        f_val += 0.25 * adaptive_condition
        
        return f_val