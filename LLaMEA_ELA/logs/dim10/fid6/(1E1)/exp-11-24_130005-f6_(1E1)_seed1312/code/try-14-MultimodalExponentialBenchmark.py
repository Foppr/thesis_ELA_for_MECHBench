import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial basis function component with multiple centers
        rbf_term = 0.0
        centers = np.linspace(-1, 1, 5)
        for i in range(5):
            for j in range(5):
                center_i = centers[i]
                center_j = centers[j]
                rbf_term += np.exp(-20 * (x_scaled[0] - center_i)**2 - 20 * (x_scaled[1] - center_j)**2)
        
        # Sinusoidal oscillations with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5 * np.pi * x_scaled[i]) * np.cos(3 * np.pi * x_scaled[i])
        
        # Cross-dimensional interaction terms with higher-order coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(x_scaled[i] * x_scaled[j])
        
        # Additional multimodal component with multiple local minima
        multi_term = 0.0
        for i in range(self.dim):
            multi_term += np.sin(15 * x_scaled[i]) * np.exp(-0.5 * x_scaled[i]**2)
        
        # Combine all terms with different weights
        return -0.3 * rbf_term + 0.4 * sin_term + 0.3 * cross_term + 0.5 * multi_term + 1.5