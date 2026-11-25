import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Radial component with enhanced sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.3 * np.sin(5 * r) + 0.2 * np.cos(2 * r))
        
        # Cross-terms between dimensions with varying frequencies and weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(x[i] * x[j] * 0.5) + 
                              0.5 * np.cos(x[i] + x[j])) * (i + j + 1) * 0.1
                
        # Adaptive gradient modulation based on position with enhanced complexity
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.2 * np.sin(x[i] * 0.3) + 0.1 * np.cos(x[i] * 0.7))
            
        # Additional multimodal component with multiple peaks and enhanced diversity
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(3 * x[i]) + 
                           0.5 * np.sin(6 * x[i]) + 
                           0.3 * np.cos(4 * x[i])) * (1 + 0.1 * i)
            
        # Add a global shaping term to improve conditioning
        shape_term = 0.05 * np.sum(x**2)
        
        # Combine all terms
        return radial_term + cross_term + grad_mod * multi_modal + shape_term + 2.0