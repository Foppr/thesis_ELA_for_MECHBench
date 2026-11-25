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
        radial_term = r**3 * (1 + 0.3 * np.cos(2 * r))
        
        # Cross-terms between dimensions with trigonometric functions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.cos(x[i] * x[j]) * (i + j + 1) * 0.5
                
        # Adaptive condition number modulation based on position
        cond_mod = 1.0
        for i in range(self.dim):
            cond_mod *= (1 + 0.4 * np.cos(x[i] * 0.3))
            
        # Additional multimodal component with multiple peaks
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += np.cos(3 * x[i]) + 0.7 * np.cos(6 * x[i])
            
        # Combine all terms
        return radial_term + cross_term + cond_mod * multi_modal + 2.0