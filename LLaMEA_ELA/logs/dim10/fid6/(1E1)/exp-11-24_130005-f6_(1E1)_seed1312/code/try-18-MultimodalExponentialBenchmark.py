import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay term that encourages convergence to center
        exp_term = np.sum(np.exp(-x_scaled**2))
        
        # Trigonometric oscillations in each dimension
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(2 * np.pi * x_scaled[i]) * np.cos(3 * np.pi * x_scaled[i])
        
        # Cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x_scaled[i] * x_scaled[j]) * np.cos(2 * x_scaled[i] + x_scaled[j])
        
        # Additional multimodal component with multiple local minima
        multi_term = 0.0
        for i in range(self.dim):
            multi_term += np.sin(10 * x_scaled[i]) * np.exp(-x_scaled[i]**2)
        
        # Chaotic sine-wave interaction term for increased complexity
        chaotic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_term += np.sin(5 * np.pi * x_scaled[i] * np.sin(3 * np.pi * x_scaled[j]))
        
        # Combine all terms with different weights
        return -0.5 * exp_term + 0.3 * trig_term + 0.2 * cross_term + 0.4 * multi_term + 0.3 * chaotic_term + 2.0