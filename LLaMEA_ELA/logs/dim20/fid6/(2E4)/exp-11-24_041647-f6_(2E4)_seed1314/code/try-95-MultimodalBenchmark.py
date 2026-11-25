import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial landscape with adaptive exponents
        polynomial_term = np.sum(np.power(np.abs(x_normalized), 2 + 0.5 * np.sin(self.dim * 0.3)))
        
        # Trigonometric modulation with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2 * (i + 1) * (1 + 0.2 * np.cos(i * 0.5))
            amp = 1.0 / (1.0 + 0.1 * i)
            trig_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.7)
        
        # Logarithmic conditioning with adaptive scaling
        log_term = 0.0
        for i in range(self.dim):
            log_term += np.log(1.0 + 0.5 * np.abs(x_normalized[i]) * (i + 1))
        
        # Cross-dimensional interaction with Gaussian kernels
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x_normalized[i] - x_normalized[j])**2 + 0.01)
                weight = 1.0 / (1.0 + 0.3 * (i + j))
                cross_term += weight * np.exp(-distance**2) * np.sin(5 * (x_normalized[i] + x_normalized[j]))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combined function with dynamic weighting
        return condition_factor * (0.4 * polynomial_term + 
                                  0.3 * trig_term + 
                                  0.2 * log_term + 
                                  0.1 * cross_term)