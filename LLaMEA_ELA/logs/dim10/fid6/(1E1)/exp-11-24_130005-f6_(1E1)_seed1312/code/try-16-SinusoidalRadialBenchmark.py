import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sum of sinusoids with increasing frequencies
        sin_sum = 0.0
        for i in range(self.dim):
            freq = i + 1
            sin_sum += np.sin(freq * np.pi * x_scaled[i]) * np.cos(freq * np.pi * x_scaled[i])
        
        # Radial basis function component with multiple centers
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                rbf_sum += np.exp(-10 * (x_scaled[i] - center)**2)
        
        # Cross-dimensional interaction terms with different weights
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-interaction
                cross_sum += np.sin(x_scaled[i] + x_scaled[j]) * np.cos(2 * x_scaled[i] - x_scaled[j])
        
        # Additional deceptive term with polynomial scaling
        poly_term = np.sum(x_scaled**4) * 0.1
        
        # Combine all terms with different weights
        return 0.5 * sin_sum + 0.3 * rbf_sum + 0.2 * cross_sum + 0.1 * poly_term + 1.0