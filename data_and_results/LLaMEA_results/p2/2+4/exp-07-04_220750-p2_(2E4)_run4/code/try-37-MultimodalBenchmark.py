import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of squares term
        sum_squares = np.sum(x_norm**2)
        
        # Product term with multiple local minima
        product_term = np.prod(np.cos(3 * x_norm))
        
        # Additional oscillatory term with higher frequency and amplitude
        oscillation = np.sum(np.sin(7 * x_norm**3))
        
        # Higher-order polynomial interaction term
        poly_term = np.sum(x_norm**8)
        
        # Cross-term interaction with increased complexity
        cross_term = np.sum(np.sin(x_norm) * np.cos(x_norm**3))
        
        # Adaptive oscillation term with variable frequency
        adaptive_osc = np.sum(np.sin(4 * x_norm) * np.cos(2 * x_norm**2))
        
        # Novel cross-dimensional coupling term
        cross_dim_coupling = np.sum(np.sin(np.sum(x_norm**2)) * np.cos(np.sum(x_norm**4)))
        
        # Enhanced multi-scale oscillation
        multi_scale_osc = np.sum(np.sin(5 * x_norm) * np.cos(3 * x_norm**2) * np.sin(x_norm**4))
        
        # Increased nonlinearity with exponential interactions
        exp_interaction = np.sum(np.exp(0.5 * x_norm**2) * np.sin(x_norm**3))
        
        # Combined terms to create enhanced multimodal landscape
        return sum_squares + 0.25 * product_term + 0.04 * oscillation + 0.1 * poly_term + 0.06 * cross_term + 0.03 * adaptive_osc + 0.05 * cross_dim_coupling + 0.02 * multi_scale_osc + 0.03 * exp_interaction