import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.noise_level = 0.1
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        sin_term += np.sum(np.sin(4 * np.pi * x_norm**2) * np.cos(5 * np.pi * x_norm**2))
        
        # Radial basis function components
        rbf_sum = 0.0
        for i in range(10):
            diff = x_norm - self.rbf_centers[i]
            rbf_sum += np.exp(-0.5 * np.sum((diff / self.rbf_widths[i])**2))
        
        # Adaptive noise component based on position
        noise = self.noise_level * np.sum(np.sin(x_norm**3) * np.cos(x_norm**4))
        
        # Cross-dimensional interaction terms
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Combined function with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + 0.01 * np.sum(x_norm**4)