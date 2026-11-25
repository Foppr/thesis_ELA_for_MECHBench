import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial component with mixed degrees and interactions
        poly_term = np.sum(x_scaled**6 + 0.7 * x_scaled**4 + 0.3 * x_scaled**2)
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        rb_term = 0.0
        for i in range(len(centers)):
            if i < self.dim:
                rb_term += np.exp(-5 * (x_scaled[i] - centers[i%len(centers)])**2)
        
        # Trigonometric component with varying frequencies and phases
        trig_term = np.sum(np.sin(8 * x_scaled) + 0.5 * np.cos(12 * x_scaled) + 0.3 * np.sin(15 * x_scaled))
        
        # Coupled oscillatory component creating complex interactions
        coupled_term = 0.0
        for i in range(self.dim - 1):
            coupled_term += np.sin(x_scaled[i] * x_scaled[i+1]) * np.cos(x_scaled[i] + x_scaled[i+1])
        
        # Sine-wave interaction between all dimensions
        interaction_term = np.sum(np.sin(np.sum(x_scaled)**2) * np.cos(np.prod(x_scaled)))
        
        # Add noise component to increase ruggedness
        noise_term = 0.1 * np.sum(np.random.rand(self.dim) * x_scaled**2)
        
        # Combine all terms with different weights
        return 0.3 * poly_term + 0.25 * rb_term + 0.2 * trig_term + 0.15 * coupled_term + 0.08 * interaction_term + 0.02 * noise_term + 3.0