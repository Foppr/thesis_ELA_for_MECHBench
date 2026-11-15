import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.noise_level = 0.15
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 15)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sinusoidal wave components with higher frequencies and varied amplitudes
        sin_term = np.sum(np.sin(4 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        sin_term += np.sum(np.sin(6 * np.pi * x_norm**1.7) * np.cos(7 * np.pi * x_norm**1.7))
        sin_term += np.sum(np.sin(8 * np.pi * x_norm**2.0) * np.cos(9 * np.pi * x_norm**2.0))
        
        # Enhanced radial basis function components with more centers
        rbf_sum = 0.0
        for i in range(15):
            diff = x_norm - self.rbf_centers[i]
            rbf_sum += np.exp(-0.5 * np.sum((diff / self.rbf_widths[i])**2))
        
        # Enhanced noise component with stronger positional dependence
        noise = self.noise_level * np.sum(np.sin(x_norm**2.8) * np.cos(x_norm**3.2))
        
        # Enhanced cross-dimensional interaction terms with stronger coupling
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += (x_norm[i]**4 + x_norm[i+1]**4) * np.sin(3 * np.pi * (x_norm[i] + x_norm[i+1]))
            cross_interaction += x_norm[i] * x_norm[i+1] * np.cos(4 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Additional higher-order polynomial terms for increased complexity
        poly_term = 0.02 * np.sum(x_norm**6)
        
        # Combined function with global minimum at origin
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + 0.01 * np.sum(np.abs(x_norm)**3)