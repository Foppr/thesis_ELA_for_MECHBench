import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial decay term that encourages convergence to center
        poly_term = np.sum(x_scaled**4)
        
        # Sinusoidal oscillations with varying frequencies
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(5 * x_scaled[i]) * np.cos(7 * x_scaled[i]) + np.sin(3 * x_scaled[i])
        
        # Higher-order cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_scaled[i]**3) * np.sin(x_scaled[j]) + (x_scaled[j]**2) * np.cos(x_scaled[i])
        
        # Additional multimodal component with multiple local minima and saddle points
        multi_term = 0.0
        for i in range(self.dim):
            multi_term += np.sin(15 * x_scaled[i]) * np.exp(-x_scaled[i]**4) + np.cos(8 * x_scaled[i])
        
        # Combine all terms with different weights
        return 0.3 * poly_term + 0.4 * trig_term + 0.2 * cross_term + 0.5 * multi_term + 3.0