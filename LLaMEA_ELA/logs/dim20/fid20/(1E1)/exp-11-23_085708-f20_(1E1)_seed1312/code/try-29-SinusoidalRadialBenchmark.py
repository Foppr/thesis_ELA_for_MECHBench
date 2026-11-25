import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Radial component with sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.5 * np.sin(3 * r))
        
        # Cross-terms between dimensions with varying frequencies
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * (i + j + 1)
                
        # Adaptive gradient modulation based on position
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.3 * np.sin(x[i] * 0.5))
            
        # Additional multimodal component with multiple peaks
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += np.sin(2 * x[i]) + 0.5 * np.sin(4 * x[i])
            
        # Combine all terms
        return radial_term + cross_term + grad_mod * multi_modal + 3.0