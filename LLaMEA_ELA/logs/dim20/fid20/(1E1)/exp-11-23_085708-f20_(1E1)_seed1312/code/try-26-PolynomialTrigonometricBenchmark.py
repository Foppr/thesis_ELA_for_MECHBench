import numpy as np

class PolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Polynomial radial component with trigonometric modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r**3 * (1 + 0.3 * np.cos(2 * r) + 0.2 * np.sin(4 * r))
        
        # Cross-terms with trigonometric functions and varying frequencies
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = (i + 1) * (j + 1)
                cross_term += np.cos(x[i] * x[j] * freq) * (1 + 0.1 * np.sin(freq * (x[i] + x[j])))
                
        # Adaptive conditioning based on position
        cond_factor = 1.0
        for i in range(self.dim):
            cond_factor *= (1 + 0.2 * np.cos(x[i] * 0.3) + 0.1 * np.sin(x[i] * 0.7))
            
        # Additional multimodal component with polynomial and trigonometric peaks
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (x[i]**4 - 6 * x[i]**2) * (1 + 0.3 * np.cos(3 * x[i]))
            
        # Combine all terms with different weights
        return radial_term + cross_term + cond_factor * multi_modal + 2.0