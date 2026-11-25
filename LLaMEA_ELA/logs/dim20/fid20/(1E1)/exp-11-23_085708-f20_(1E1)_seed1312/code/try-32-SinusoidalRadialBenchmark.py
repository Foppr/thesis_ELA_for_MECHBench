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
        radial_term = r * (1 + 0.7 * np.sin(4 * r) + 0.3 * np.cos(2 * r))
        
        # Cross-terms between dimensions with modified frequencies and weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j] * 0.5) * (i + j + 1) * 0.8
                
        # Adaptive gradient modulation with enhanced position sensitivity
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.4 * np.sin(x[i] * 0.7) + 0.2 * np.cos(x[i] * 1.3))
            
        # Additional multimodal component with increased peak complexity
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += np.sin(3 * x[i]) + 0.6 * np.sin(6 * x[i]) + 0.3 * np.cos(2 * x[i])
            
        # Add a quadratic shift term to increase landscape curvature
        shift_term = 0.1 * np.sum(x**2)
        
        # Combine all terms
        return radial_term + cross_term + grad_mod * multi_modal + shift_term + 2.5