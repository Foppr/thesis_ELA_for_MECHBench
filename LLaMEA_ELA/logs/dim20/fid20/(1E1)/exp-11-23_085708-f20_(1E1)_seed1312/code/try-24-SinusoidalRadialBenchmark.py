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
        radial_term = r * (1 + 0.7 * np.sin(4 * r))
        
        # Cross-terms between dimensions with varying frequencies and weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j] * 0.5) * (i + j + 1) * 0.3
                
        # Adaptive gradient modulation with stronger position dependence
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.8))
            
        # Additional multimodal component with higher frequency and amplitude
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 1.2 * np.sin(3 * x[i]) + 0.8 * np.sin(6 * x[i])
            
        # Add a small constant shift to avoid trivial solutions
        constant_shift = 2.5
        
        # Combine all terms
        return radial_term + cross_term + grad_mod * multi_modal + constant_shift