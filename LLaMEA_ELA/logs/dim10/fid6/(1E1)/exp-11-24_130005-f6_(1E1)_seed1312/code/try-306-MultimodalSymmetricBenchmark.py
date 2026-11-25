import numpy as np

class MultimodalSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with symmetric oscillations
        r = np.sqrt(np.sum(x_scaled**2))
        radial = 2.0 * np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Trigonometric oscillation pattern in each dimension
        trig_sum = 0.0
        for i in range(self.dim):
            trig_sum += np.sin(x_scaled[i] * 4.0) * np.cos(x_scaled[i] * 3.0)
            
        # Exponential barrier terms creating multiple local minima
        barrier = 0.0
        for i in range(self.dim):
            # Multiple exponential barriers at different positions
            barrier += np.exp(-10.0 * (x_scaled[i] - 0.5)**2) + \
                      np.exp(-10.0 * (x_scaled[i] + 0.5)**2) + \
                      np.exp(-5.0 * x_scaled[i]**2)
        
        # Cross-term interactions creating complex coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x_scaled[i] * x_scaled[j] * 2.0) * \
                             np.cos(x_scaled[i] - x_scaled[j])
        
        # Sine-cosine product with varying frequencies
        freq_product = 0.0
        for i in range(self.dim):
            freq_product += np.sin(x_scaled[i]) * np.cos(2.0 * x_scaled[i]) * \
                           np.sin(3.0 * x_scaled[i])
        
        # Combine all components with different weights
        return 1.5 * radial + 1.0 * trig_sum + 0.8 * barrier + 0.6 * cross_term + 0.4 * freq_product