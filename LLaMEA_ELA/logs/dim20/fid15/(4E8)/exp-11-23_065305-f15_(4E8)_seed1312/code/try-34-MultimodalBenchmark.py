import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stable computation
        x_scaled = x / 5.0
        
        # Nested exponential decay with sinusoidal modulation
        exp_nested = np.sum(np.exp(-x_scaled**2) * np.sin(5 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Higher-order trigonometric polynomial creating ultra-mulitmodal structure
        high_order_trig = np.sum(np.sin(6 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled) + 
                                np.sin(4 * np.pi * x_scaled**2) * np.cos(3 * np.pi * x_scaled**2))
        
        # Coupled saddle-point structures with cross-dimensional interactions
        cross_saddle = np.sum(x_scaled**4 * np.sin(x_scaled) * np.cos(x_scaled) + 
                             x_scaled**6 * np.sin(x_scaled**2) * np.cos(x_scaled**2))
        
        # Additional polynomial coupling term for increased complexity
        poly_coupling = np.sum(x_scaled**7 * np.sin(2 * x_scaled) + x_scaled**3 * np.cos(5 * x_scaled))
        
        # Combine all terms with varying weights
        result = 0.3 * exp_nested + 0.25 * high_order_trig + 0.25 * cross_saddle + 0.2 * poly_coupling
        
        return result