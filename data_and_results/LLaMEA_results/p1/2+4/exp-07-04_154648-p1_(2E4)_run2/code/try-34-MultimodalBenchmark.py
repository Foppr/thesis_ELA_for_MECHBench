import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.noise_level = 0.15
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (12, dim))
        self.rbf_widths = np.random.uniform(0.3, 1.8, 12)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        sin_term += np.sum(np.sin(5 * np.pi * x_norm**1.5) * np.cos(6 * np.pi * x_norm**1.5))
        
        # Radial basis function components
        rbf_sum = 0.0
        for i in range(12):
            diff = x_norm - self.rbf_centers[i]
            rbf_sum += np.exp(-0.5 * np.sum((diff / self.rbf_widths[i])**2))
        
        # Adaptive noise component based on position
        noise = self.noise_level * np.sum(np.sin(x_norm**2.5) * np.cos(x_norm**3.5))
        
        # Cross-dimensional interaction terms with modified interaction strength
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += (x_norm[i]**3 + x_norm[i+1]**3) * np.sin(2 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Combined function with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + 0.02 * np.sum(x_norm**5)